def is_prime(n):
    if n in (2, 3):
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[25]
    primes = []
    for n in reversed(range(2, x)):
        if is_prime(n):
            n_str = str(n)
            if '0' not in n_str:
                trunc = n_str
                while trunc:
                    if not is_prime(int(trunc)):
                        break
                    trunc = trunc[1:]
                else:
                    primes.append(n)
    return primes