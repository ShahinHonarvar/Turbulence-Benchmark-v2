def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[55]
    truncatable_primes = []
    for possiblePrime in range(2, x):
        if '0' in str(possiblePrime):
            continue
        all_primes = True
        num_str = str(possiblePrime)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                all_primes = False
                break
        if all_primes:
            truncatable_primes.append(possiblePrime)
    return sorted(truncatable_primes)