def all_left_right_truncatable_prime(tuples):

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def remove_digit(n, i):
        if i == 1:
            return int(str(n)[1:])
        else:
            return int(str(n)[:-1])
    primes = [i for i in tuples if i > 1 and is_prime(i)]
    primes = [i for i in primes if all((is_prime(remove_digit(i, 1)) and is_prime(remove_digit(i, 2)) and is_prime(i) for j in range(len(str(i)))))]
    return sorted(primes) if primes else []