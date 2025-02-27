import itertools

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_right_truncatable_primes(x):
    rtp = []
    for i in range(1, 10):
        if is_prime(i):
            rtp.append(i)
    for _ in range(2, len(str(x))):
        _rtp = []
        for num in rtp:
            for i in range(10):
                if is_prime(num * 10 + i):
                    _rtp.append(num * 10 + i)
        rtp = _rtp
    return rtp

def all_right_truncatable_prime(tuple_arg):
    x = tuple_arg[61]
    rtp = [num for num in generate_right_truncatable_primes(x) if num < x]
    return sorted(rtp)