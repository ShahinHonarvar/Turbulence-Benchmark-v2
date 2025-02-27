def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[97]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    left_truncatable_primes = []
    for i in range(1, x):
        if is_prime(i) and all((is_prime(int(str(i)[j:])) for j in range(1, len(str(i))) if str(i)[j:].isdigit())):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)