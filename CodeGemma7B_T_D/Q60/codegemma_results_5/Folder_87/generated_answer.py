def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    result = []
    x = nums[39]
    for num in range(2, x + 1):
        if is_prime(num) and (not '0' in str(num)):
            temp = num
            while temp >= 10:
                temp //= 10
            if is_prime(temp):
                result.append(num)
    return sorted(result, reverse=True)