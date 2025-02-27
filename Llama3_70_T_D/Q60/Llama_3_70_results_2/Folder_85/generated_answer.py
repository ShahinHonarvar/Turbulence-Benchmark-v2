def all_left_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = num_tuple[94]
    primes = [i for i in range(2, x + 1) if is_prime(i) and '0' not in str(i)]
    left_right_truncatable_primes = []
    for prime in primes:
        prime_str = str(prime)
        if len(prime_str) > 1:
            is_truncatable = True
            while len(prime_str) > 1:
                prime_str = prime_str[1:-1]
                if not is_prime(int(prime_str)) or '0' in prime_str:
                    is_truncatable = False
                    break
            if is_truncatable:
                left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes)