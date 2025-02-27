def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_right_truncatable_prime(num):
    num_str = str(num)
    for i in range(len(num_str)):
        if not is_prime(int(num_str[:i] + num_str[i + 1:])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    start, end = (numbers[0], numbers[3])
    truncatable_primes = []
    for num in range(end, start - 1, -1):
        if left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes