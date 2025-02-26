def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[65]
    result = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_truncatable = True
        str_num = str(num)
        while len(str_num) > 1:
            str_num = str_num[1:-1]
            if not is_prime(int(str_num)):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            left_keep = str(num)
            right_keep = str(num)
            while len(left_keep) > 1:
                left_keep = left_keep[1:]
                if not is_prime(int(left_keep)):
                    is_truncatable = False
                    break
            while len(right_keep) > 1:
                right_keep = right_keep[:-1]
                if not is_prime(int(right_keep)):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(num)
    return sorted(result, reverse=True)