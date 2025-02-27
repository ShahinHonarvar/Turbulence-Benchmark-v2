def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[42]
    primes = []
    for n in range(2, x + 1):
        if '0' in str(n):
            continue
        truncated = n
        while truncated >= 2:
            if not is_prime(truncated):
                break
            truncated = int(str(truncated)[1:-1])
        else:
            primes.append(n)
    return sorted(primes)