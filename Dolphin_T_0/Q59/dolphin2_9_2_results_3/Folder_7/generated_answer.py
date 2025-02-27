def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

def all_left_truncatable_prime(p):
    x = p[803]
    prime = [2]
    if x < 2:
        return prime
    for n in range(3, x):
        if is_prime(n):
            s = str(n)
            if '0' not in s:
                for c in s:
                    if not is_prime(int(s)):
                        break
                    s = s[1:]
                if len(s) == 0:
                    prime.append(n)
    return sorted(prime)