def is_left_truncatable_prime(num):
    if '0' in str(num):
        return False
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    num_str = str(num)
    if len(num_str) > 1:
        return is_left_truncatable_prime(int(num_str[1:]))
    return True

def all_left_truncatable_prime(nums):
    x = nums[0]
    result = []
    for i in range(x - 1, 1, -1):
        if is_left_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result