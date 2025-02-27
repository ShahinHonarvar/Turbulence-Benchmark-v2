def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    if n < 2:
        return False
    n_str = str(n)
    for i in range(len(n_str) - 1, 0, -1):
        if not is_prime(int(n_str[i:])):
            return False
    return True

def all_right_truncatable_prime(lst):
    x = lst[38]
    primes = [i for i in range(2, x) if is_prime(i) and is_truncatable(i)]
    return sorted(primes, reverse=True)