def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[14]
    result = []
    for num in range(10, x):
        str_num = str(num)
        is_left_truncatable = True
        for i in range(len(str_num)):
            truncated = int(str_num[i:])
            if not is_prime(truncated):
                is_left_truncatable = False
                break
        if is_left_truncatable and all((digit != '0' for digit in str_num)):
            result.append(num)
    return sorted(result)