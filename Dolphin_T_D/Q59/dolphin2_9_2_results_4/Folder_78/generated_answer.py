def all_left_truncatable_prime(t):
    x = t[23]
    left_truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x):
        str_i = str(i)
        if '0' not in str_i:
            if is_prime(i):
                for j in range(1, len(str_i)):
                    if not is_prime(int(str_i[j:])):
                        break
                else:
                    left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)