def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[30]
    right_truncatable_primes = []
    for num in range(2, x):
        if all((int(str(num)[:-i]) for i in range(1, len(str(num))) if num % i == 0 and num > 10 ** i)):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)