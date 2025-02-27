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

def find_primes_between_indices(nums):
    if len(nums) < 81 or len(nums) < 66:
        return []
    primes = [num for num in nums[65:82] if is_prime(num)]
    return sorted(primes)