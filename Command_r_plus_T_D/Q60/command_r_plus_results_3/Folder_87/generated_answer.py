def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_right_truncate(num):
    str_num = str(num)
    left_truncate = str_num
    right_truncate = str_num
    for i in range(len(str_num)):
        left_truncate = left_truncate[1:]
        right_truncate = right_truncate[:-1]
        if not is_prime(int(left_truncate)) or not is_prime(int(right_truncate)):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    for num in numbers:
        if num > 1 and num < 10:
            if is_prime(num):
                truncatable_primes.append(num)
        elif num >= 10:
            if is_prime(num) and left_right_truncate(num):
                truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes