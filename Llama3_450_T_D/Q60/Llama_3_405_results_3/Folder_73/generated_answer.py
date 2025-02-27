def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[97]
    truncatable_primes = []
    for possiblePrime in range(11, x + 1):
        if '0' in str(possiblePrime):
            continue
        prime = True
        num_str = str(possiblePrime)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:-i or None])):
                prime = False
                break
        if prime and is_prime(possiblePrime):
            truncatable_primes.append(possiblePrime)
    return truncatable_primes