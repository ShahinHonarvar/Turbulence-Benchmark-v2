def prime_factors(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_set = set()
    prime_factors = nums[29]
    for i in range(2, prime_factors):
        while prime_factors % i == 0:
            if is_prime(i):
                prime_set.add(i)
            prime_factors //= i
    if is_prime(prime_factors):
        prime_set.add(prime_factors)
    return prime_set