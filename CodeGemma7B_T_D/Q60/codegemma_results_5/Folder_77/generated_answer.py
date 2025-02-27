from functools import reduce

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable(n):
    for i in range(1, len(str(n))):
        if not is_prime(int(str(n)[:i])):
            return False
    return True

def right_truncatable(n):
    for i in range(1, len(str(n))):
        if not is_prime(int(str(n)[-i:])):
            return False
    return True

def all_left_right_truncatable_prime(tuples):
    nums = []
    for num in tuples:
        if left_truncatable(num) and right_truncatable(num):
            nums.append(num)
    return sorted(nums, reverse=True)