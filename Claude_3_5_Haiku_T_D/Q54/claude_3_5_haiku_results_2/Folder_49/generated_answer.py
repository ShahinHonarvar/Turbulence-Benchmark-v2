def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[14]
    result = []
    for num in range(2, x):
        if is_prime(num):
            truncated = num
            is_right_truncatable = True
            while truncated > 9:
                truncated //= 10
                if not is_prime(truncated):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                result.append(num)
    return sorted(result)