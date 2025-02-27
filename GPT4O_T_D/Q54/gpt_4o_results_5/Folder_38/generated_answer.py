def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def right_truncatable(prime):
    str_num = str(prime)
    return all((is_prime(int(str_num[:i])) for i in range(1, len(str_num) + 1)))

def all_right_truncatable_prime(numbers):
    if len(numbers) <= 28:
        return []
    x = numbers[28]
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num) and right_truncatable(num):
            truncatable_primes.append(num)
    return truncatable_primes