def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_truncatable_prime(n):
    if '0' in str(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[1:]) if len(str(n)) > 1 else 0
    return True

def all_left_truncatable_prime(nums):
    if len(nums) <= 69:
        return []
    x = nums[69]
    result = [n for n in range(1, x) if is_left_truncatable_prime(n)]
    result.sort(reverse=True)
    return result