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
            current = num
            while current > 0:
                current //= 10
                if current > 0 and (not is_prime(current)):
                    truncatable = False
                    break
            if truncatable:
                result.append(num)
    return result