def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[7]
    result = []
    for num in range(2, x):
        if all((is_prime(int(str(num)[i:])) for i in range(len(str(num))))) and '0' not in str(num):
            result.append(num)
    return sorted(result)