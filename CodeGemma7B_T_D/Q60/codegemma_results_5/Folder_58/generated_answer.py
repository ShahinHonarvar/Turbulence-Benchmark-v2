from math import sqrt

def left_truncatable_prime(n):
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

def right_truncatable_prime(n):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not left_truncatable_prime(int(str_n[i:])):
            return False
    return True

def all_left_right_truncatable_prime(n):
    prime_list = []
    for i in range(2, n + 1):
        if left_truncatable_prime(i) and right_truncatable_prime(i):
            prime_list.append(i)
    prime_list.sort(reverse=True)
    return prime_list