def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[94]
    right_truncatable_primes = []
    for possiblePrime in range(2, x):
        if is_prime(possiblePrime):
            num_str = str(possiblePrime)
            truncated_num_str = num_str
            while len(truncated_num_str) > 1:
                truncated_num_str = truncated_num_str[:-1]
                if not is_prime(int(truncated_num_str)):
                    break
            else:
                right_truncatable_primes.append(possiblePrime)
    return sorted(right_truncatable_primes)