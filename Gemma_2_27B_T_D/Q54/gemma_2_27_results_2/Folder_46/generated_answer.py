def all_right_truncatable_prime(nums):
    x = nums[33]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            is_right_truncatable = True
            n = i
            while n > 0:
                if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or (not is_prime):
                    is_right_truncatable = False
                    break
                n //= 10
            if is_right_truncatable:
                primes.append(i)
    return sorted(primes)