def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[69]

    def is_truncatable_prime(n):
        num_str = str(n)
        if '0' in num_str:
            return False
        for i in range(1, len(num_str)):
            if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:-i])):
                return False
        return True
    truncatable_primes = [i for i in range(2, x + 1) if is_truncatable_prime(i) and is_prime(i)]
    return sorted(truncatable_primes, reverse=True)