def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(n):
    str_n = str(n)
    for _ in range(len(str_n) - 1):
        str_n = str_n[1:-1]
        if not is_prime(int(str_n)) or '0' in str_n:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    limit = numbers[33]
    truncatable_primes = [i for i in range(10, limit + 1) if is_prime(i) and is_left_right_truncatable(i)]
    return truncatable_primes