def all_left_truncatable_prime(int_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = int_tuple[7]
    left_truncatable_primes = []
    for i in range(2, x):
        if i % 5 != 0 and all((is_prime(int(str(i)[j:])) for j in range(len(str(i))))):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)