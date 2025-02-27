def all_left_truncatable_prime(tuple_of_integers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tuple_of_integers[93]
    left_truncatable_primes = []
    for i in range(2, x):
        if '0' not in str(i):
            str_i = str(i)
            is_left_truncatable_prime = True
            for j in range(1, len(str_i)):
                if not is_prime(int(str_i[j:])):
                    is_left_truncatable_prime = False
                    break
            if is_left_truncatable_prime and is_prime(i):
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)