def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[54]
    left_truncatable_primes = [i for i in range(2, x) if str(i).find('0') == -1 and all((is_prime(int(str(i)[j:])) for j in range(len(str(i)))))]
    return sorted(left_truncatable_primes)