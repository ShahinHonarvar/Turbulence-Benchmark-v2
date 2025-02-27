def is_prime(n):
    if n in (2, 3):
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(n):
    if n in (2, 3):
        return True
    n_string = str(n)
    if '0' in n_string:
        return False
    for i in range(len(n_string)):
        if not is_prime(int(n_string[i:]) * (n_string[i:] != '')):
            return False
        if not is_prime(int(n_string[:i]) * (n_string[:i] != '')):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[35]
    Primes = [i for i in range(2, x + 1) if is_left_right_truncatable(i)]
    return sorted(Primes, reverse=True)