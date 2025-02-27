import itertools

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(x):
    primes = []
    for i in itertools.count(1):
        if not is_prime(i):
            continue
        str_i = str(i)
        if int(str_i[-1]) >= 5:
            continue
        if i >= x:
            break
        primes.append(i)
        for j in range(1, len(str_i)):
            if not is_prime(int(str_i[j:])):
                break
    return sorted(primes)

def all_right_truncatable_prime(n):
    return right_truncatable_prime(n[39])