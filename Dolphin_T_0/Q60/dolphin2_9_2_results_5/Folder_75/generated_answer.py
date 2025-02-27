def is_prime(n):
    if n in (2, 3):
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[41]
    primes = []
    for i in range(1, x + 1):
        if is_prime(i) and i % 10 != 0:
            s = str(i)
            for _ in range(len(s) - 2):
                if not is_prime(int(s[1:]) * 10) or not is_prime(int(s[:-1]) // 10):
                    break
                s = s[1:-1]
            else:
                primes.append(i)
    return sorted(primes)