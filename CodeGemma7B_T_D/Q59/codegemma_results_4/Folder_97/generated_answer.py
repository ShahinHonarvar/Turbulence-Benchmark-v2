def all_left_truncatable_prime(num):
    truncatable_primes = []
    for x in range(2, num):
        str_x = str(x)
        if '0' not in str_x and all((int(str_x[i:]) in range(2, x) for i in range(1, len(str_x)))):
            truncatable_primes.append(x)
    return sorted(truncatable_primes)