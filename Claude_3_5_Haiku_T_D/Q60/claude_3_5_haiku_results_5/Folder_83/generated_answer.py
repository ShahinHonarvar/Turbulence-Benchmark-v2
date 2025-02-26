def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[24]
    result = []
    for num in range(2, x + 1):
        if is_prime(num):
            str_num = str(num)
            is_truncatable = True
            for i in range(1, len(str_num)):
                left_truncate = int(str_num[i:])
                right_truncate = int(str_num[:-i])
                if not (is_prime(left_truncate) and is_prime(right_truncate)):
                    is_truncatable = False
                    break
            if is_truncatable and '0' not in str_num:
                result.append(num)
    return sorted(result)