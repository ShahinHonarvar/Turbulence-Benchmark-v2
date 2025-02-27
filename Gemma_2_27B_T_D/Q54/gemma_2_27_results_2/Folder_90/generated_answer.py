from collections import deque

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[466]
    result = []
    for i in range(2, x):
        if prime(i):
            n = str(i)
            flag = True
            while len(n) > 1:
                n = n[:-1]
                if not prime(int(n)):
                    flag = False
                    break
            if flag:
                result.append(i)
    return sorted(result, reverse=True)