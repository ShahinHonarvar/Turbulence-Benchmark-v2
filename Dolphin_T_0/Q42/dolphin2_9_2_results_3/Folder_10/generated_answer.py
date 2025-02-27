def is_prime(n):
    if n < 2:
        return False
    for i in range(2, round(pow(n, 0.5)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(nums):
    num = nums[54]
    prime_set = set()
    for i in range(1, num + 1):
        if num % i == 0 and is_prime(i):
            prime_set.add(i)
    return prime_set