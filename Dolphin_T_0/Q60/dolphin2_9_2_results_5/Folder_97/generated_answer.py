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

def is_left_right_truncatable_prime(p):
    p_str = str(p)
    if '0' in p_str:
        return False
    while len(p_str) > 2:
        if not is_prime(int(p_str)):
            return False
        if p_str[0] == p_str[-1]:
            return False
        p_str = p_str[1:-1]
    return True

def all_left_right_truncatable_prime(tuples):
    x = tuples[645]
    primes = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)