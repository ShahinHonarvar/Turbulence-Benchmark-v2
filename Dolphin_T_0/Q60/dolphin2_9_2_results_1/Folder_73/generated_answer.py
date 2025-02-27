def all_left_right_truncatable_prime(numbers_tuple):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n == 1:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True
    x = numbers_tuple[97]
    primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            trunc = str(i)
            if '0' in trunc:
                continue
            while len(trunc) > 1:
                if not is_prime(int(trunc[1:-1])):
                    break
                trunc = trunc[1:-1]
            else:
                primes.append(i)
    return sorted(primes)