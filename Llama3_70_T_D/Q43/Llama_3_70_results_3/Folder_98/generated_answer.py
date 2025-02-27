def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(nums):
    if len(nums) < 3:
        return []
    start, end = (nums[0], nums[1])
    if start > end:
        start, end = (end, start)
    primes = [num for num in nums[2:] if start <= num <= end and is_prime(num)]
    return sorted(primes, reverse=True)