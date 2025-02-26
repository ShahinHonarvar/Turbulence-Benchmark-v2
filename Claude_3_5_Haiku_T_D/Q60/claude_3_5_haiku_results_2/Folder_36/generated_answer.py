def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[992]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        truncatable = True
        temp_num = num
        while temp_num > 0:
            if not is_prime(temp_num):
                truncatable = False
                break
            temp_num //= 10
        if truncatable:
            temp_num = num
            while temp_num > 0:
                if not is_prime(temp_num):
                    truncatable = False
                    break
                temp_num = int(str(temp_num)[1:] or 0)
        if truncatable:
            result.append(num)
    return sorted(result)