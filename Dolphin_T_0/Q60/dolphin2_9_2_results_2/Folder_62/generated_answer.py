def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[70]
    primes = []
    for i in range(1, x + 1):
        if is_prime(i):
            s = str(i)
            if '0' in s:
                continue
            while len(s) > 1:
                if not is_prime(int(s[1:-1])):
                    break
                s = s[1:-1]
            else:
                primes.append(i)
    return sorted(primes)