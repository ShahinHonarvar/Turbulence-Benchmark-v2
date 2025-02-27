def all_right_truncatable_prime(nums):
    x = nums[89]
    primes = []
    for num in range(2, x):
        is_prime = True
        temp = num
        while temp > 0:
            if temp not in primes:
                is_prime = False
                break
            temp = temp // 10
        if is_prime:
            primes.append(num)
    return sorted(primes, reverse=True)