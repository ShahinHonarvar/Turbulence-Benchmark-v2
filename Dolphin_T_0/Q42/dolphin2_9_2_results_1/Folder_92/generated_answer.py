def prime_factors(nums):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def factors(num):
        result = set()
        for i in range(2, num + 1):
            if num % i == 0 and is_prime(i) and is_prime(num // i):
                result.add(i)
        return result
    return factors(nums[0])