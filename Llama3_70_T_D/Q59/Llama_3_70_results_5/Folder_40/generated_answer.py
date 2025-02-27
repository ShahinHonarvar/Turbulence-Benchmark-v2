def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[10]
    primes = [i for i in range(2, x) if is_prime(i) and '0' not in str(i)]
    lt_primes = []
    for p in primes:
        p_str = str(p)
        for i in range(1, len(p_str)):
            if not is_prime(int(p_str[i:])):
                break
        else:
            lt_primes.append(p)
    return sorted(lt_primes, reverse=True)