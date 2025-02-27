def all_right_truncatable_prime(nums):
    x = nums[758]
    primes = []
    for num in range(2, x):
        is_prime = True
        temp = num
        while temp > 0:
            if temp % 2 == 0 and temp != 2:
                is_prime = False
                break
            for i in range(3, int(temp ** 0.5) + 1, 2):
                if temp % i == 0:
                    is_prime = False
                    break
            if not is_prime:
                break
            temp //= 10
        if is_prime:
            primes.append(num)
    return sorted(primes)