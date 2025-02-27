def _is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def _is_left_truncatable_prime(num):
    if '0' in str(num):
        return False
    length = len(str(num))
    for i in range(length):
        if not _is_prime(int(str(num)[i:])):
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[54]
    results = []
    for num in range(2, x):
        if _is_left_truncatable_prime(num):
            results.append(num)
    return sorted(results, reverse=True)