def all_left_truncatable_prime(t):
    x = t[7]
    primes = [2, 3, 5, 7]
    n = 1
    while True:
        n1 = n + 1
        while True:
            str_n = str(n1)
            if len(str_n) != len(set(str_n)) or '0' in str_n:
                n1 += 1
                continue
            flag = True
            for e in range(0, len(str_n)):
                if not is_prime(int(str_n[e:])):
                    flag = False
                    break
            if flag:
                primes.append(n1)
            n1 += 1
            if n1 > 10 ** len(str(x)):
                break
        n *= 10
        if n > 10 ** (len(str(x)) - 1):
            break
    return sorted([p for p in primes if p < x])

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