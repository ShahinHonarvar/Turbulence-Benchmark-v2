def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[64]
    result = []
    for num in range(x - 1, 1, -1):
        temp = num
        is_right_truncatable = True
        while temp > 0:
            if not is_prime(temp):
                is_right_truncatable = False
                break
            temp //= 10
        if is_right_truncatable and is_prime(num):
            result.append(num)
    return result