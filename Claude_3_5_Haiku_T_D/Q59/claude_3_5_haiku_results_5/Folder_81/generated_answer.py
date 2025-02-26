def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[98]
    result = []
    for n in range(2, x):
        if '0' not in str(n):
            truncatable = True
            temp = n
            while temp > 0:
                if not is_prime(temp):
                    truncatable = False
                    break
                temp //= 10
            if truncatable:
                result.append(n)
    return sorted(result)