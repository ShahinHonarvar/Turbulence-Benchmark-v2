def all_right_truncatable_prime(nums):
    x = nums[55]
    primes = []
    for i in range(2, x):
        if all((not i % j for j in range(2, int(i ** 0.5) + 1))):
            is_right_truncatable = True
            n = i
            while n > 0:
                if n % 2 == 0 or any((n % j == 0 for j in range(3, int(n ** 0.5) + 1, 2))):
                    is_right_truncatable = False
                    break
                n //= 10
            if is_right_truncatable:
                primes.append(i)
    return sorted(primes)