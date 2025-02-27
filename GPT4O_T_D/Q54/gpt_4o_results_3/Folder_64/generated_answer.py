def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_primes(upper_limit):
    candidates = [2, 3, 5, 7]
    result = []
    while candidates:
        candidate = candidates.pop(0)
        if candidate < upper_limit:
            if is_prime(candidate):
                result.append(candidate)
                for digit in '1379':
                    candidates.append(int(str(candidate) + digit))
    return result

def all_right_truncatable_prime(numbers):
    x = numbers[4]
    primes = right_truncatable_primes(x)
    return sorted(primes)