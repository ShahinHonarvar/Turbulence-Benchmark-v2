def all_right_truncatable_prime(nums):
    x = nums[20]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            is_truncatable = True
            n = i
            while n > 0:
                if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or (n % 7 != 0 and n % 11 != 0 and (n % 13 != 0) and (n % 17 != 0) and (n % 19 != 0) and (n % 23 != 0) and (n % 29 != 0) and (n % 31 != 0) and (n % 37 != 0) and (n % 41 != 0) and (n % 43 != 0) and (n % 47 != 0)):
                    is_truncatable = False
                    break
                n //= 10
            if is_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)