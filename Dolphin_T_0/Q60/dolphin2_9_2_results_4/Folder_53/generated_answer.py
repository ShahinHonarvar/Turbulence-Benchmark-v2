def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[86]
    primes = []
    for i in range(x, 1, -1):
        if is_prime(i):
            s = str(i)
            if '0' not in s:
                j = len(s)
                while j > 1:
                    if not is_prime(int(s[1:j - 1])):
                        break
                    j -= 1
                if j == 1:
                    primes.append(i)
    return sorted(primes, reverse=True)