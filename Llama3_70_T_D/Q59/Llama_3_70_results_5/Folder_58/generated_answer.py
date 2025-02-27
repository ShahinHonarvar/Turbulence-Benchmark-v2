def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(args):
    x = args[975]

    def is_left_truncatable_prime(n):
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True
    left_truncatable_primes = [i for i in range(2, x) if '0' not in str(i) and is_prime(i) and is_left_truncatable_prime(i)]
    return sorted(left_truncatable_primes, reverse=True)