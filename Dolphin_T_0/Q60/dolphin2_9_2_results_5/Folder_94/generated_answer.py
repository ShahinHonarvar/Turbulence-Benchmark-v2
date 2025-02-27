def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[43]
    primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            str_i = str(i)
            if '0' not in str_i:
                while len(str_i) > 1:
                    if not is_prime(int(str_i[1:-1])):
                        break
                    str_i = str_i[1:-1]
                else:
                    primes.append(i)
    return sorted(primes)