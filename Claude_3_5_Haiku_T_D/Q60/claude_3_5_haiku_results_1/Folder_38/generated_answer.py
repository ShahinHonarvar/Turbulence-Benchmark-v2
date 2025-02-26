def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[28]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        is_truncatable = True
        n = num
        while n > 0:
            if not is_prime(n):
                is_truncatable = False
                break
            n //= 10
        if is_truncatable:
            str_num = str(num)
            for i in range(len(str_num)):
                trunc_num = int(str_num[i:])
                if not is_prime(trunc_num):
                    is_truncatable = False
                    break
        if is_truncatable:
            result.append(num)
    return sorted(result)