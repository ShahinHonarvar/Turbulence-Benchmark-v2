def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_truncatable_prime(num):
    str_num = str(num)
    while str_num:
        if not is_prime(int(str_num)):
            return False
        str_num = str_num[1:]
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[74]
    left_truncatable_primes = []
    for number in range(2, x):
        if '0' not in str(number) and is_left_truncatable_prime(number):
            left_truncatable_primes.append(number)
    return left_truncatable_primes