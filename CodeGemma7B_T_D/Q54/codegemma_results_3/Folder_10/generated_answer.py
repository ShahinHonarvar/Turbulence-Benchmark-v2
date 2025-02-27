from math import sqrt

def is_prime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def truncated_prime(n):
    digits = [int(d) for d in str(n)]
    for i in range(len(digits)):
        number = int(''.join((str(d) for d in digits[i:])))
        if is_prime(number):
            return number
    return None

def all_right_truncatable_prime(x):
    prime_list = [n for n in range(2, x) if is_prime(n)]
    trun_list = []
    for prime in prime_list:
        truncated = truncated_prime(prime)
        if truncated is not None:
            trun_list.append(truncated)
    trun_list.sort(reverse=True)
    return trun_list