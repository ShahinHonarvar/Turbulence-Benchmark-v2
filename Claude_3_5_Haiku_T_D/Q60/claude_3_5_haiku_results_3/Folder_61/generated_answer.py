def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[3]
    result = []
    for num in range(x, 11, -1):
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
            length = len(str(num))
            while length > 1:
                temp_num %= 10 ** (length - 1)
                if not is_prime(temp_num):
                    truncatable = False
                    break
                length -= 1
            if truncatable:
                result.append(num)
    return result