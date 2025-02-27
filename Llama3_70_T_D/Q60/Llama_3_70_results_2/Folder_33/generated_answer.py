def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[945]
    primes = [i for i in range(2, x + 1) if is_prime(i) and '0' not in str(i)]
    left_right_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        while len(str_prime) > 2:
            str_prime = str_prime[1:-1]
            if not is_prime(int(str_prime)):
                break
        else:
            left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes, reverse=True)