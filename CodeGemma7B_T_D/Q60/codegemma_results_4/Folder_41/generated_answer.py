def all_left_right_truncatable_prime(numberTuple):
    x = numberTuple[46]
    prime_numbers = []
    for num in range(2, x + 1):
        if is_prime(num):
            if is_truncatable(num):
                prime_numbers.append(num)
    prime_numbers.sort(reverse=True)
    return prime_numbers if prime_numbers else []

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_truncatable(num):
    str_num = str(num)
    if '0' in str_num:
        return False
    for i in range(1, len(str_num)):
        left_truncation = int(str_num[i:])
        if not is_prime(left_truncation):
            return False
        right_truncation = int(str_num[:-i])
        if not is_prime(right_truncation):
            return False
    return True