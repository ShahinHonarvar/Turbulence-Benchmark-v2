def all_left_truncatable_prime(t):
    x = t[7]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    ltp_primes = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        num_str = str(i)
        if all((is_prime(int(num_str[j:])) for j in range(1, len(num_str)))):
            ltp_primes.append(i)
    return sorted(ltp_primes)