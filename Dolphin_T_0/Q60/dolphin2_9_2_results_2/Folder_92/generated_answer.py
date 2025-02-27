def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[7]
    primes = []
    for i in range(2, x + 1):
        if '0' not in str(i) and is_prime(i) and (str(i) in [str(int(str(i)[1:n])) for n in range(1, len(str(i))) if is_prime(int(str(i)[1:n]))]):
            primes.append(i)
    return sorted(primes)