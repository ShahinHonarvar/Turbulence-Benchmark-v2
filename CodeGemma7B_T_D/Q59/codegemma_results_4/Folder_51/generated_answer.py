def all_left_truncatable_prime(numbers):
    primes = [i for i in numbers if is_prime(i)]
    left_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        if not str_prime.startswith('0'):
            for i in range(1, len(str_prime)):
                truncated_prime = int(str_prime[i:])
                if not is_prime(truncated_prime):
                    break
            else:
                left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True