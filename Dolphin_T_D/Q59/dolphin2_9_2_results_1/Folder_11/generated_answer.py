def all_left_truncatable_prime(numbers_tuple):

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

    def truncates_to_primes(num):
        return all((is_prime(num[n:]) for n in range(len(str(num))))) and str(num)[0] != '0'
    x = numbers_tuple[86]
    return sorted([num for num in range(2, x) if is_prime(num) and truncates_to_primes(num)])