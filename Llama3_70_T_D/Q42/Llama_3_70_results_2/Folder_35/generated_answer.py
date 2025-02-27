def prime_factors(nums):

    def get_prime_factors(num):
        i = 2
        factors = set()
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                factors.add(i)
        if num > 1:
            factors.add(num)
        return factors
    return get_prime_factors(nums[993])