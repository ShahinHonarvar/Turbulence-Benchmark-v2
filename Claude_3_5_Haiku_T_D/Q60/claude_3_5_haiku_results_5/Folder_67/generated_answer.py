def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[71]
    result = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_left_right_truncatable = True
        original_num = num
        while num > 9:
            num //= 10
            if not is_prime(num):
                is_left_right_truncatable = False
                break
        if not is_prime(num):
            is_left_right_truncatable = False
        num = original_num
        while len(str(num)) > 1:
            num = int(str(num)[1:])
            if not is_prime(num):
                is_left_right_truncatable = False
                break
        if is_left_right_truncatable and is_prime(original_num):
            result.append(original_num)
    return result