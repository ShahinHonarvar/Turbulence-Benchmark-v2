def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[97]
    result = []
    for num in range(2, x):
        if is_prime(num):
            truncatable = True
            temp = num
            while temp > 0:
                temp //= 10
                if temp > 0 and (not is_prime(temp)):
                    truncatable = False
                    break
            if truncatable:
                result.append(num)
    return sorted(result)