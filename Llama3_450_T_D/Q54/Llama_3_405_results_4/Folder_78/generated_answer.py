def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[23]
    right_truncatable_primes = []
    for possiblePrime in range(2, x):
        if is_prime(possiblePrime):
            num = str(possiblePrime)
            truncatable = True
            for i in range(1, len(num)):
                if not is_prime(int(num[:-i])):
                    truncatable = False
                    break
            if truncatable:
                right_truncatable_primes.append(possiblePrime)
    return sorted(right_truncatable_primes)