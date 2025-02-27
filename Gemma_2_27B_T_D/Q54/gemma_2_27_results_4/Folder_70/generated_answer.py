def all_right_truncatable_prime(nums):
    x = nums[433]
    primes = []
    for i in range(x, 1, -1):
        n = i
        is_prime = True
        while n > 0:
            if n < 2 or any((n % j == 0 for j in range(2, int(n ** 0.5) + 1))):
                is_prime = False
                break
            n //= 10
        if is_prime:
            primes.append(i)
    return sorted(primes, reverse=True)