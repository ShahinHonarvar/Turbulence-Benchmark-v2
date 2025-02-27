def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[4]
    primes = [2]
    for i in range(3, x):
        if is_prime(i):
            s = str(i)
            for j in s[1:]:
                if '0' in s[1:]:
                    break
                if not is_prime(int(s[1:])):
                    break
                s = s[1:]
            else:
                primes.append(i)
    return sorted(primes)