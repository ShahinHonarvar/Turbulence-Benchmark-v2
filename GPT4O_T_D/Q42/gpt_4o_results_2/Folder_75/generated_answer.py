def prime_factors(nums):

    def find_prime_factors(n):
        factors = set()
        divisor = 2
        while n >= 2:
            if n % divisor == 0:
                factors.add(divisor)
                n //= divisor
            else:
                divisor += 1
        return factors
    integer_at_index_80 = nums[80]
    return find_prime_factors(integer_at_index_80)