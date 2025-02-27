def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[70]
    truncatable_primes = []
    for possiblePrime in range(2, x):
        if is_prime(possiblePrime):
            num_str = str(possiblePrime)
            truncatable = True
            for i in range(len(num_str)):
                trunc_str = num_str[:-i - 1]
                if trunc_str and (not is_prime(int(trunc_str))):
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.append(possiblePrime)
    return sorted(truncatable_primes, reverse=True)