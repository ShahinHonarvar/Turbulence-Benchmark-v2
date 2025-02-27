def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def is_right_truncatable_prime(num):
    if not is_prime(num):
        return False
    num_str = str(num)
    while len(num_str) > 1:
        num_str = num_str[:-1]
        if not is_prime(int(num_str)):
            return False
    return True

def all_right_truncatable_prime(numbers):
    if len(numbers) <= 14:
        return []
    x = numbers[14]
    truncatable_primes = [num for num in range(2, x) if is_right_truncatable_prime(num)]
    return sorted(truncatable_primes, reverse=True)