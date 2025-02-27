def prime_factors(nums):
    return set((factor for num in nums for factor in factorize_int(num) if num == nums[80]))

def factorize_int(num):
    factors = set()
    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            factors.add(i)
            num //= i
    return factors