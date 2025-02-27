def is_prime(num):
    if num <= 1:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def is_truncatable_prime(num):
    str_num = str(num)
    if '0' in str_num:
        return False
    for i in range(len(str_num)):
        left_truncate = int(str_num[i:])
        right_truncate = int(str_num[:len(str_num) - i])
        if not is_prime(left_truncate) or not is_prime(right_truncate):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) <= 36:
        return []
    x = numbers[36]
    truncatable_primes = []
    for num in range(10, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes