def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    n_str = str(n)
    for i in range(1, len(n_str)):
        if not is_prime(int(n_str[i:])):
            return False
    return True

def all_right_truncatable_prime(x):
    prime_list = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            prime_list.append(i)
    return sorted(prime_list)