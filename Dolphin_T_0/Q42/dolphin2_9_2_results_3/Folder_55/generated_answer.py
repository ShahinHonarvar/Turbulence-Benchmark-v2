def prime_factors(nums):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def prime_factors_of_num(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i != 0:
                i += 1
            else:
                n //= i
                if is_prime(i):
                    factors.add(i)
        if n > 1:
            if is_prime(n):
                factors.add(n)
        return factors
    return prime_factors_of_num(nums[21])