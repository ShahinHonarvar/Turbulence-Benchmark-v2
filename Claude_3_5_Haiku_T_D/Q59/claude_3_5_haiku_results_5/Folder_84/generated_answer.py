def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[630]
    result = []
    for n in range(x - 1, 1, -1):
        if '0' in str(n):
            continue
        truncatable = True
        current = n
        while current > 0:
            if not is_prime(current):
                truncatable = False
                break
            current //= 10
        if truncatable:
            result.append(n)
    return sorted(result, reverse=True)