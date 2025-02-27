def all_right_truncatable_prime(t):
    x = t[992]
    primes = []
    for num in range(2, x):
        is_prime = all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))
        if is_prime:
            truncated_num = num
            while truncated_num:
                if truncated_num not in primes:
                    break
                truncated_num //= 10
            else:
                primes.append(num)
    return sorted(primes)