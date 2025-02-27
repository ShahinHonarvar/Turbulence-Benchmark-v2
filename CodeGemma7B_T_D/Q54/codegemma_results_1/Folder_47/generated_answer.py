from math import sqrt

def all_right_truncatable_prime(nums):
    inte = nums[49]
    sol = []
    for i in range(2, inte):
        for j in range(1, i):
            if isprime(i) and isprime(i - j):
                sol.append(i)
    return sorted(sol)

def isprime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, int(sqrt(n)) + 2, 2):
        if n % i == 0:
            return False
    return True