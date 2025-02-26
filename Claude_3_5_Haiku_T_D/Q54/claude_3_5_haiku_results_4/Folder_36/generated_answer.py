def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[992]
    result = []
    for n in range(2, x):
        is_truncatable = True
        temp = n
        while temp > 0:
            if not is_prime(temp):
                is_truncatable = False
                break
            temp //= 10
        if is_truncatable and is_prime(n):
            result.append(n)
    return sorted(result)