def all_left_right_truncatable_prime(int_tuple):

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
    x = int_tuple[4]
    truncable_primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            trunc = str(i)
            while len(trunc) > 1:
                if not is_prime(int(trunc[1:-1])):
                    break
                trunc = trunc[1:-1]
            else:
                truncable_primes.append(i)
    return sorted(truncable_primes)