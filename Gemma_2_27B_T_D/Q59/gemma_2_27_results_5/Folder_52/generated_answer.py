from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(nums):
    x = nums[52]
    primes = []
    for i in range(x, 1, -1):
        if is_prime(i):
            is_left_truncatable = True
            num_str = str(i)
            for j in range(1, len(num_str)):
                if not is_prime(int(num_str[j:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)