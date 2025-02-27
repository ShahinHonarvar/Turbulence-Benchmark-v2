import itertools

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

def is_right_truncatable_prime(n):
    return all((is_prime(int(str(n)[:i])) for i in range(1, len(str(n)) + 1)))

def all_right_truncatable_prime(t):
    x = t[14]
    result = [i for i in itertools.islice((i for i in itertools.count(1) if is_right_truncatable_prime(i)), x)]
    return sorted(result, reverse=True)