def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_right_truncatable_prime(num):
    num_str = str(num)
    for i in range(1, len(num_str)):
        if not is_prime(int(num_str[:i])) or not is_prime(int(num_str[i:])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    for num in numbers:
        if num > 1 and left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes