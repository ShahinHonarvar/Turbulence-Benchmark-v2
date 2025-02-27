def prime_factors(nums):
    return {f for f in factor(nums[54]) if is_prime(f)}

def factor(n):
    m = 2
    for i in range(2, n):
        if n % i == 0:
            result = factor(n // i)
            result.add(i)
            return result
    return {n}

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True