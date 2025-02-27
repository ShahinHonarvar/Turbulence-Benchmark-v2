def all_left_right_truncatable_prime(lst_of_tuples):
    x = lst_of_tuples[433]
    left_right_primes = []
    for num in range(2, x + 1):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            for i in range(1, len(str(num)) - 1):
                if all((int(str(num)[i]) % i != 0 for i in range(2, int(int(str(num)[i]) ** 0.5) + 1))):
                    left_right_primes.append(num)
    return sorted(left_right_primes, reverse=True)