def all_left_truncatable_prime(x):
    prime = [True for i in range(x + 1)]
    prime[0] = prime[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if prime[i]:
            for j in range(i * 2, x + 1, i):
                prime[j] = False
    res = [i for i in range(x) if prime[i] and (not str(i).startswith('0')) and is_left_truncatable_prime(i)]
    res.sort()
    return res

def is_left_truncatable_prime(n):
    if n == 0 or n % 2 == 0:
        return False
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not prime[int(str_n[i:])]:
            return False
    return True