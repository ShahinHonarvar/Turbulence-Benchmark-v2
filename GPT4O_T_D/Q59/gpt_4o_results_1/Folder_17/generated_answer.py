def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_truncatable_prime(num):
    if '0' in str(num):
        return False
    original_num = num
    while num > 0:
        if not is_prime(num):
            return False
        num //= 10
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[36]
    truncatable_primes = [n for n in range(2, x) if is_left_truncatable_prime(n)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes