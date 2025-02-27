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

def is_truncatable_prime(num):
    if '0' in str(num):
        return False
    str_num = str(num)
    length = len(str_num)
    for i in range(length):
        if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:length - i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[945]
    truncatable_primes = []
    for num in range(11, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)