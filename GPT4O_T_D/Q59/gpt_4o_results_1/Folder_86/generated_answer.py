def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_truncatable_prime(num):
    str_num = str(num)
    while str_num:
        if not is_prime(int(str_num)):
            return False
        str_num = str_num[1:]
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[126]
    left_truncatable_primes = []
    for i in range(2, x):
        if '0' not in str(i) and is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)