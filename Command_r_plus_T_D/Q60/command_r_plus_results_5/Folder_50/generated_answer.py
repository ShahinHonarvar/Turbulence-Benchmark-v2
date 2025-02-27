def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    str_num = str(num)
    for i in range(len(str_num)):
        if not is_prime(int(str_num[:i] + str_num[i + 1:])) or not is_prime(int(str_num[i:])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    start, end = numbers
    if start < 2:
        start = 2
    truncatable_primes = []
    for num in range(end, start - 1, -1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes