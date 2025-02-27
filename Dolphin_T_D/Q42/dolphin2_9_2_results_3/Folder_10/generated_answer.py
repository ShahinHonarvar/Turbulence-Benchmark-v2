def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_factors(nums):
    prime_set = set()
    for num in nums:
        prime_set.add(num)
    return prime_set