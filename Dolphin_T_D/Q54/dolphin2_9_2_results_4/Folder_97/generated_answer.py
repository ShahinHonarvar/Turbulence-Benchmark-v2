def all_right_truncatable_prime(tuple):
    x = tuple[645]
    primes = []
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, num))):
            truncated_num = int(str(num)[:-1])
            if truncated_num != 0 and all((truncated_num % i != 0 for i in range(2, truncated_num))):
                primes.append(num)
    return sorted(primes)