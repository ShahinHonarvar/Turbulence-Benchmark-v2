def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[79]
    result = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        if is_prime(num):
            is_truncatable = True
            for i in range(1, len(str(num))):
                left_trunc = int(str(num)[i:])
                if not is_prime(left_trunc):
                    is_truncatable = False
                    break
            for i in range(len(str(num))):
                right_trunc = int(str(num)[:i])
                if right_trunc > 0 and (not is_prime(right_trunc)):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(num)
    return sorted(result, reverse=True)