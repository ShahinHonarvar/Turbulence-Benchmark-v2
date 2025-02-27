def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncate_left(n):
    return int(str(n)[1:])

def truncate_right(n):
    return int(str(n)[:-1])

def all_left_right_truncatable_prime(numbers):
    x = numbers[14]
    trunc_primes = []
    for n in range(2, x + 1):
        if '0' in str(n):
            continue
        trunc_n = n
        while trunc_n > 0:
            if not is_prime(trunc_n):
                break
            trunc_n = truncate_left(trunc_n)
        else:
            trunc_n = n
            while trunc_n > 0:
                if not is_prime(trunc_n):
                    break
                trunc_n = truncate_right(trunc_n)
            else:
                trunc_primes.append(n)
    return sorted(trunc_primes, reverse=True)