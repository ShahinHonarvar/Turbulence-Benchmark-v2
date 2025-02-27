def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[28]
    primes = [i for i in range(2, x + 1) if is_prime(i) and '0' not in str(i)]
    truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        while len(str_prime) > 2:
            str_prime = str_prime[1:-1]
            if not is_prime(int(str_prime)):
                break
        else:
            truncatable_primes.append(prime)
    return truncatable_primes