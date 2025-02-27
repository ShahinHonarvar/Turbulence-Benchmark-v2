from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[50]
    primes = []
    for i in range(2, x + 1):
        s = str(i)
        if '0' not in s:
            is_truncatable = True
            while len(s) > 1:
                if not (is_prime(int(s)) and is_prime(int(s[1:]))):
                    is_truncatable = False
                    break
                s = s[1:-1]
            if is_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)