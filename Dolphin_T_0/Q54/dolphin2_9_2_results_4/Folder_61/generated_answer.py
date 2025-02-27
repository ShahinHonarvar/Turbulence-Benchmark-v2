def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    n = str(n)
    for i in range(len(n) - 1):
        if not is_prime(int(n[:i + 1])):
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[3]
    result = [i for i in range(x) if is_prime(i) and is_right_truncatable(i)]
    result.sort(reverse=True)
    return result