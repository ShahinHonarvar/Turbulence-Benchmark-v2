def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[100]
    primes = [i for i in range(x, 1, -1) if is_prime(i)]
    left_right_truncatable_primes = []
    for prime in primes:
        while prime > 9:
            if is_prime(prime // 10) and is_prime(prime % 10):
                left_right_truncatable_primes.append(prime)
                break
            else:
                prime = prime // 10 + 10 * (prime % 10)
    return sorted(left_right_truncatable_primes, reverse=True)