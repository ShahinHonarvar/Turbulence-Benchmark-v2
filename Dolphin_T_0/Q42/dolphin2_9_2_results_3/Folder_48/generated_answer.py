def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(nums):
    target_index = 247
    target_num = nums[target_index]
    prime_factors_set = set()
    for i in range(1, target_num + 1):
        if target_num % i == 0 and is_prime(i):
            prime_factors_set.add(i)
    return prime_factors_set