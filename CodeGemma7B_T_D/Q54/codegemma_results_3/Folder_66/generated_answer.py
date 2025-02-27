from math import sqrt

def all_right_truncatable_prime(nums):
    ans = []
    num = int(''.join((str(i) for i in nums[25])))
    for i in range(num, 0, -1):
        if is_prime(i):
            if all((is_prime(int(str(i)[:-j])) for j in range(1, len(str(i))))):
                ans.append(i)
    return sorted(ans, reverse=True)

def is_prime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True