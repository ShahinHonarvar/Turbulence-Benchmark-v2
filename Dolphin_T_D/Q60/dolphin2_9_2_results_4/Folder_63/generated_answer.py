def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[88]
    primes = []
    for i in range(2, x + 1):
        str_i = str(i)
        if '0' not in str_i:
            while len(str_i) > 1 and is_prime(int(str_i)):
                str_i = str_i[1:-1]
                if len(str_i) >= 2 and '0' not in str_i and is_prime(int(str_i)):
                    primes.append(i)
    return sorted(primes)