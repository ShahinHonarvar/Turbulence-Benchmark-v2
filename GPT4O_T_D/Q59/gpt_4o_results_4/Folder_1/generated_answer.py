def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(p):
    str_p = str(p)
    while str_p:
        if not is_prime(int(str_p)):
            return False
        str_p = str_p[1:]
    return True

def all_left_truncatable_prime(nums):
    x = nums[20]
    left_truncatable_primes = []
    for num in range(1, x):
        if '0' in str(num):
            continue
        if is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)