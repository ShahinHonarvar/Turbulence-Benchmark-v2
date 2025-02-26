def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[30]
    result = []
    for num in range(x - 1, 1, -1):
        if not is_prime(num):
            continue
        truncatable = True
        temp = num
        while temp > 0:
            temp //= 10
            if temp > 0 and (not is_prime(temp)):
                truncatable = False
                break
        if truncatable:
            result.append(num)
    return result