def all_left_truncatable_prime(arg):
    x = arg[96]
    left_truncatable_prime = []
    for i in range(2, x):
        if is_prime(i) and (not str(i).startswith('0')) and left_truncatable(i):
            left_truncatable_prime.append(i)
    return sorted(left_truncatable_prime, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable(n):
    str_n = str(n)
    for j in range(1, len(str_n)):
        if not is_prime(int(str_n[j:])):
            return False
    return True