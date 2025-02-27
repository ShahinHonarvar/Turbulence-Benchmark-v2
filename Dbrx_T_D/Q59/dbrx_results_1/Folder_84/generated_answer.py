import itertools

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    return all(map(is_prime, (n % 10 ** i for i in range(1, len(str(n)) + 1))))

def all_left_truncatable_prime(t):
    x = list(itertools.islice((i for i in itertools.count(1) if is_prime(i)), 630))[0]
    return sorted(filter(left_truncatable_prime, range(1, x)), reverse=True)