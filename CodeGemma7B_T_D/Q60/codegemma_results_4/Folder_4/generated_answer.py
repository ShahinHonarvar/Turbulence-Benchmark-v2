def all_left_right_truncatable_prime(x):
    d = {0, 2, 5}
    p = [2, 3, 5, 7, 11, 13, 17, 19, 23] + [i for i in range(29, int(x) + 1, 2) if i % 3 != 0]
    result = []
    for i in p:
        if isprime(i) and is_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    if n < 10:
        return False
    if 0 in str(n):
        return False

    def isprime_recur(n):
        if n in d:
            return True
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    s, e = (str(n), str(n))
    while int(s) >= 10 and int(e) >= 10:
        s = s[1:]
        e = e[:-1]
        if not isprime_recur(int(s)) or not isprime_recur(int(e)):
            return False
    return True