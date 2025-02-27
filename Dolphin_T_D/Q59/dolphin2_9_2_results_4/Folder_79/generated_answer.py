def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    str_n = str(n)
    while len(str_n) > 1:
        if not is_prime(int(str_n[1:])):
            return False
        str_n = str_n[1:]
    return is_prime(int(str_n))

def all_left_truncatable_prime(t):
    x = t[91]
    prime_numbers = []
    for i in range(1, x + 1):
        if is_truncatable_prime(i):
            prime_numbers.append(i)
    prime_numbers.sort()
    return prime_numbers