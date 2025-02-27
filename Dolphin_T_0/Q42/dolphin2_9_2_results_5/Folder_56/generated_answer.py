def prime_factors(nums):

    def is_prime(n):
        if n != 1 and n != 0 and (n % 2 != 0):
            for i in range(3, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True
        return False
    factors = []
    num = nums[60]
    for i in range(1, num + 1):
        if num % i == 0 and is_prime(i):
            factors.append(i)
    return set(factors)