def prime_factors(nums):
    return set((factor for num in nums for factor in prime_factorize(num) if num % 20 == 9))

def prime_factorize(num):
    factors = set()
    for i in range(2, num + 1):
        if num % i == 0:
            factors.add(i)
            while num % i == 0:
                num //= i
    return factors