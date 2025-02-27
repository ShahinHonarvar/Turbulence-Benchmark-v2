def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[23]
    primes = []
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, num))):
            trunc = num
            while trunc > 0:
                if all((trunc % i != 0 for i in range(2, trunc))):
                    primes.append(trunc)
                    trunc //= 10
                else:
                    break
    return sorted(list(set(primes)))