def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[8]
    result = []
    for num in range(x, 11, -1):
        if '0' not in str(num):
            is_truncatable = True
            for left_trunc_len in range(len(str(num)) - 1, 0, -1):
                left_trunc = int(str(num)[left_trunc_len:])
                if not is_prime(left_trunc):
                    is_truncatable = False
                    break
            for right_trunc_len in range(len(str(num)) - 1, 0, -1):
                right_trunc = int(str(num)[:right_trunc_len])
                if not is_prime(right_trunc):
                    is_truncatable = False
                    break
            if is_truncatable and is_prime(num):
                result.append(num)
    return result