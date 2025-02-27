def all_right_truncatable_prime(nums):
    x = nums[14]
    primes = []
    for i in range(2, x):
        is_prime = True
        n = i
        while n > 0:
            if n < 2 or (n % 2 == 0 and n > 2) or all((n % j for j in range(3, int(n ** 0.5) + 1, 2))):
                is_prime = False
                break
            n //= 10
        if is_prime:
            primes.append(i)
    return sorted(primes, reverse=True)