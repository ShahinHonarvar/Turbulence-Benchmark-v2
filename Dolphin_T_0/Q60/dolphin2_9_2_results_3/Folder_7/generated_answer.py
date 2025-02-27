def all_left_right_truncatable_prime(numbers_tuple):

    def is_prime(n):
        if n in (2, 3) or n % 2 != 0:
            for i in range(3, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    return False
        else:
            return False
        return True
    x = numbers_tuple[803]
    primes = []
    for i in range(2, x + 1):
        if not '0' in str(i) and is_prime(i):
            if len(str(i)) > 2 and is_prime(i) and is_prime(int(str(i)[1:-1])):
                primes.append(i)
            else:
                continue
    return sorted(primes)