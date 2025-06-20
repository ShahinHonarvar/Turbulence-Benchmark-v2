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
        left_trunc = int(num_str[i:])
        right_trunc = int(num_str[:-i])
        if not is_prime(left_trunc) or not is_prime(right_trunc):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    max_val = numbers[81]
    truncatable_primes = []
    for num in range(max_val, 1, -1):
        if num % 10 == 0:
            continue
        if is_prime(num) and left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes