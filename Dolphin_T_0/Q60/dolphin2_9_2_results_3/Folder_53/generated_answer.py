def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[86]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            trunc = num
            while trunc != 0:
                if trunc < 10 and trunc not in left_right_truncatable_primes:
                    left_right_truncatable_primes.append(trunc)
                trunc //= 10
                if all((trunc % i != 0 for i in range(2, int(trunc ** 0.5) + 1))):
                    left_right_truncatable_primes.append(trunc)
                trunc %= 10
    return sorted(left_right_truncatable_primes, reverse=True)