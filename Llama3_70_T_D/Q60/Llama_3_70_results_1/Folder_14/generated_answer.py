def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    n_str = str(n)
    if '0' in n_str:
        return False
    for i in range(1, len(n_str)):
        if not is_prime(int(n_str[i:])) or not is_prime(int(n_str[:-i])):
            return False
    return is_prime(n)

def all_left_right_truncatable_prime(numbers):
    x = numbers[78]
    truncatable_primes = [i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)]
    return sorted(truncatable_primes, reverse=True)