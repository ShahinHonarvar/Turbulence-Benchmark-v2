def all_left_truncatable_prime(lst):
    x = lst[97]
    left_truncatable_primes = []
    for num in range(2, x):
        if all([num % i != 0 for i in range(2, num)]):
            trunc = num
            while trunc > 0:
                if not all([trunc % i != 0 for i in range(2, trunc)]):
                    break
                trunc //= 10
            else:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)