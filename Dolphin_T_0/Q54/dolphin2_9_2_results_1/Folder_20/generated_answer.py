def all_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[100]

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9:
            return True
        if n % 3 == 0:
            return False
        r = int(n ** 0.5)
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True

    def is_right_truncatable_prime(n):
        if is_prime(n):
            for i in range(1, len(str(n))):
                if not is_prime(int(str(n)[-i:])):
                    return False
            return True
    right_truncatable_primes = []
    for n in range(2, x):
        if is_right_truncatable_prime(n):
            right_truncatable_primes.append(n)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes