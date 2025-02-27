def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(t):
    x = t[97]
    primes = []
    for n in range(1, x + 1):
        if '0' in str(n):
            continue
        if is_prime(n):
            truncated = n
            while truncated > 1:
                truncated = int(str(truncated)[1:-1])
                if '0' in str(truncated):
                    break
                if not is_prime(truncated):
                    break
            else:
                primes.append(n)
    return sorted(primes, reverse=True)