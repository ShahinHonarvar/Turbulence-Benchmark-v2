def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[11]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        is_truncatable = True
        working_num = num
        while working_num > 9:
            working_num //= 10
            if not is_prime(working_num):
                is_truncatable = False
                break
        if not is_prime(working_num):
            is_truncatable = False
        working_num = num
        while working_num > 9:
            working_num %= 10 ** (len(str(working_num)) - 1)
            if not is_prime(working_num):
                is_truncatable = False
                break
        if is_prime(num) and is_truncatable:
            result.append(num)
    return sorted(result)