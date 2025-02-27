def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    strn = str(n)
    for i in range(len(strn) - 1):
        if not is_prime(int(strn[i + 1:])) or not is_prime(int(strn[:i + 1])):
            return False
    return True

def all_left_right_truncatable_prime(arg):
    x = arg[433]
    primes = [i for i in reversed(range(2, x + 1)) if is_prime(i) and is_truncatable(i)]
    return primes