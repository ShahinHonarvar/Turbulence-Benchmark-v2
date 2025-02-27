def all_right_truncatable_prime(nums):
    x = nums[32]
    primes = []
    for num in range(2, x):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            temp = num
            while temp > 0:
                if temp % 2 == 0:
                    break
                temp //= 10
            else:
                primes.append(num)
    return sorted(primes)