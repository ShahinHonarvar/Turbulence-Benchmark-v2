def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(n_tuple):
    x = n_tuple[33]
    primes_lt = []
    for i in range(x):
        if is_prime(i):
            i_str = str(i)
            if '0' in i_str:
                continue
            while i_str:
                if not is_prime(int(i_str)):
                    break
                i_str = i_str[1:]
            else:
                primes_lt.append(i)
    primes_lt.sort()
    return primes_lt