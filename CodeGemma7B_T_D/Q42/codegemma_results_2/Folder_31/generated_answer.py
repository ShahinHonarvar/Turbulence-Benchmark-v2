def prime_factors(nums):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    prime_factors = set()
    for num in nums:
        for i in range(2, int(num ** 0.5) + 1):
            while num % i == 0:
                if is_prime(i):
                    prime_factors.add(i)
                num //= i
    return prime_factors