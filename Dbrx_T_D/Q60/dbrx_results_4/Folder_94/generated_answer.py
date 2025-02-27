def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_and_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    if not is_prime(n):
        return False
    for i in range(len(str(n)) - 1):
        if not is_prime(int(str(n)[i:])):
            return False
    for j in range(len(str(n)) - 1):
        if not is_prime(int(str(n)[:-j - 1])):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    max_num = max(nums)
    result = []
    for i in range(3, max_num + 1, 2):
        if is_left_and_right_truncatable_prime(i):
            result.append(i)
    return result