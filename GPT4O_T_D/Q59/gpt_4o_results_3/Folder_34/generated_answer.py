def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    while str_n:
        if not is_prime(int(str_n)):
            return False
        str_n = str_n[1:]
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[18]
    ltp_numbers = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            ltp_numbers.append(num)
    return sorted(ltp_numbers, reverse=True)