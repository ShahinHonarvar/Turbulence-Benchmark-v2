def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[100]
    result = []
    for num in range(10, x + 1):
        if '0' in str(num):
            continue
        is_truncatable = True
        temp = num
        while temp > 0:
            if not is_prime(temp):
                is_truncatable = False
                break
            temp //= 10
        temp = num
        digit_count = len(str(temp))
        while digit_count > 1:
            temp %= 10 ** (digit_count - 1)
            digit_count -= 1
            if not is_prime(temp):
                is_truncatable = False
                break
        if is_truncatable:
            result.append(num)
    return sorted(result)