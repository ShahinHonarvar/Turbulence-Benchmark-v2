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

def prime_factors(nums):
    if not isinstance(nums, list) or len(nums) <= 87:
        return 'Invalid input'
    num = nums[87]
    factors = set()
    for i in range(2, num + 1):
        if num % i == 0 and is_prime(i):
            factors.add(i)
    return factors