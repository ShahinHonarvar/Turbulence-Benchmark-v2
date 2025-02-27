from math import sqrt

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[97]
    result = []
    for i in range(2, x):
        if is_prime(i) and all((is_prime(int(str(i)[:-j])) for j in range(1, len(str(i))))):
            result.append(i)
    return sorted(result, reverse=True)