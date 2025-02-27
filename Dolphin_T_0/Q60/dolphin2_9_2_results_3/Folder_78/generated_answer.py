def is_prime(n):
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

def all_left_right_truncatable_prime(args):
    x = args[23]
    primes = []
    for n in range(2, x + 1):
        if x < 10:
            break
        if is_prime(n):
            n_str = str(n)
            if '0' in n_str:
                continue
            while len(n_str) > 1:
                n = int(n_str[1:-1])
                n_str = str(n)
                if not is_prime(n):
                    break
            else:
                primes.append(n)
    return sorted(primes)