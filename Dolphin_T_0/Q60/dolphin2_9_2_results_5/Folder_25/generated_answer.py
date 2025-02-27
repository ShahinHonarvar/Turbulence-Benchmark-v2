def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    n_str = str(n)
    length = len(n_str)
    if length == 1:
        return is_prime(n)
    for i in range(length - 1):
        if n_str[i] == '0':
            return False
        if not is_prime(int(n_str[i + 1:])) or not is_prime(int(n_str[:i + 1])):
            return False
    return True

def all_left_right_truncatable_prime(arg):
    x = arg[92]
    primes = [i for i in range(2, x + 1) if is_truncatable_prime(i)]
    return sorted(primes)