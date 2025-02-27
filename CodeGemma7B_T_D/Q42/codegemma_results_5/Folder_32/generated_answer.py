def prime_factors(nums):
    prime_factorized_849 = set()
    prime_factorized_849.update(factors(nums[849]))
    return prime_factorized_849

def factors(n):
    result = set()
    low = 2
    high = (n + 1) // 2
    while low < high:
        if n % low == 0:
            result.add(low)
            if low != high:
                result.add(high)
        low += 1
        high -= 1
    return result