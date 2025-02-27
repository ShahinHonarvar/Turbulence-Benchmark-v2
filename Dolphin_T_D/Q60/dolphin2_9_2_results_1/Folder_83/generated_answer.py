def all_left_right_truncatable_prime(tuple_of_positive_integers):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    x = tuple_of_positive_integers[24]
    left_right_truncatable_primes = []
    for possible_prime in range(2, x + 1):
        if '0' not in str(possible_prime):
            while possible_prime > 1:
                if is_prime(possible_prime):
                    left_right_truncatable_primes.append(possible_prime)
                    possible_prime = int(str(possible_prime)[1:-1])
                else:
                    break
    left_right_truncatable_primes.sort()
    return left_right_truncatable_primes