def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[32]
    result = []
    for num in range(2, x):
        if is_prime(num):
            trunc_num = num
            is_right_truncatable = True
            while trunc_num > 0:
                trunc_num //= 10
                if trunc_num > 0 and (not is_prime(trunc_num)):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                result.append(num)
    return sorted(result)