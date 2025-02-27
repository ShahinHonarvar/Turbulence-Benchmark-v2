from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[6]
    primes = []
    for i in range(x - 1, 0, -1):
        if is_prime(i):
            str_i = str(i)
            if '0' not in str_i and all((is_prime(int(str_i[0:j])) for j in range(1, len(str_i)))):
                primes.append(i)
    return primes