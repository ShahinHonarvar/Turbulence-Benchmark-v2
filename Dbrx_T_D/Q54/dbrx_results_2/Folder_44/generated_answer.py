def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_right_truncatable_primes(x):
    right_truncatable_primes = []
    for i in range(1, 10):
        if is_prime(i):
            right_truncatable_primes.append(i)
        for j in range(1, 10):
            num = i * 10 + j
            if num < x and is_prime(num):
                right_truncatable_primes.append(num)
    return list(set(right_truncatable_primes))

def all_right_truncatable_prime(tup):
    x = tup[39]
    rtp = generate_right_truncatable_primes(x)
    rtp.sort()
    return rtp