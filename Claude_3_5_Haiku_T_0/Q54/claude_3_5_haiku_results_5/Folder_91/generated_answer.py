def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[0]
    result = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            truncatable = True
            truncated = num
            while truncated > 9:
                truncated //= 10
                if not is_prime(truncated):
                    truncatable = False
                    break
            if truncatable:
                result.append(num)
    return result