def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[14]
    result = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_truncatable = True
        curr_num = num
        while curr_num > 9:
            curr_num //= 10
            if not is_prime(curr_num):
                is_truncatable = False
                break
        if not is_prime(curr_num):
            is_truncatable = False
        if is_truncatable:
            curr_num = num
            while curr_num > 9:
                curr_num %= 10 ** (len(str(curr_num)) - 1)
                if not is_prime(curr_num):
                    is_truncatable = False
                    break
            if is_truncatable and is_prime(num):
                result.append(num)
    return result