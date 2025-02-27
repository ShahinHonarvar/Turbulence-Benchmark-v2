def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_truncatable_prime(num):
    if '0' in str(num):
        return False
    str_num = str(num)
    for i in range(len(str_num)):
        if not is_prime(int(str_num[i:])):
            return False
    return True

def all_left_truncatable_prime(t):
    if len(t) < 56:
        return []
    x = t[55]
    left_truncatable_primes = []
    for number in range(2, x):
        if is_left_truncatable_prime(number):
            left_truncatable_primes.append(number)
    return left_truncatable_primes