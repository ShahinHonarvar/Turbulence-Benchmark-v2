def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(args):
    x = args[39]
    primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            if i % 10 != 0 and i // 10 % 10 != 0 and all((is_prime(i // 10 ** j) and i % 10 ** (j + 1) != 0 and (i // 10 ** (j + 1) % 10 != 0) for j in range(1, len(str(i))))):
                primes.append(i)
    return sorted(primes)