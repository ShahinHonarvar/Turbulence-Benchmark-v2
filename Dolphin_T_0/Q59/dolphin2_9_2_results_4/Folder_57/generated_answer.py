def all_left_truncatable_prime(input_tuple):

    def is_truncatable_prime(n):
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        rev_n = int(''.join(reversed(str(n))))
        return is_truncatable_prime(rev_n)
    x = input_tuple[54]
    primes = [2]
    for n in range(3, x):
        if all((n % p != 0 for p in primes)):
            primes.append(n)
            if is_truncatable_prime(n):
                trunc_primes.append(n)
    return sorted(trunc_primes, reverse=True)