def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_right_truncatable_prime(num):
    str_num = str(num)
    for i in range(len(str_num)):
        left_part = str_num[:i]
        right_part = str_num[-i:]
        if not is_prime(int(left_part)) or not is_prime(int(right_part)):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    for num in numbers:
        if num > 0 and left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)