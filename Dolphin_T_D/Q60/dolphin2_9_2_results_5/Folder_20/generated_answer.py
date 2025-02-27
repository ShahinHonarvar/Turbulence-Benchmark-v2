def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def all_left_right_truncatable_prime(n_tuple):
    x = n_tuple[100]
    primes = []
    for i in range(x, 1, -1):
        if is_prime(i):
            str_i = str(i)
            while len(str_i) > 1:
                str_i = str_i[1:-1]
                if not is_prime(int(str_i)):
                    break
            else:
                primes.append(i)
    return primes