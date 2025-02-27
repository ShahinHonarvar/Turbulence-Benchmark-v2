def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_right_truncate(num):
    left_truncate = num
    right_truncate = num
    str_num = str(num)
    for _ in range(len(str_num) - 1):
        left_truncate //= 10
        right_truncate %= 10 ** len(str_num[:-1])
        if not is_prime(left_truncate) or not is_prime(right_truncate):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    start, end = numbers
    truncatable_primes = []
    for num in range(end, start - 1, -1):
        if num < 10:
            if is_prime(num):
                truncatable_primes.append(num)
        elif str(num).count('0') == 0 and is_prime(num) and left_right_truncate(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)