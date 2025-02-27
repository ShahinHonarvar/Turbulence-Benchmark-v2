def all_left_truncatable_prime(t):
    x = t[784]
    primes = [2]

    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for current in range(3, int(n ** 0.5) + 1, 2):
            if n % current == 0:
                return False
        return True
    for possible_prime in range(3, x, 2):
        if '0' in str(possible_prime):
            continue
        if all((is_prime(int(str(possible_prime)[i:])) for i in range(1, len(str(possible_prime))))):
            primes.append(possible_prime)
    return primes