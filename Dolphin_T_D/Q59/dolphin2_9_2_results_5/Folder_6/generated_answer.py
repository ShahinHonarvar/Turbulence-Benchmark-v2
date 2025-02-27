def all_left_truncatable_prime(tup):
    x = tup[74]
    left_truncatable_primes = []
    for num in range(2, x):
        if all_digits_non_zero(num) and is_truncatable_prime(num):
            left_truncatable_primes.append(num)
    left_truncatable_primes.sort()
    return left_truncatable_primes

def all_digits_non_zero(num):
    for digit in str(num):
        if digit == '0':
            return False
    return True

def is_truncatable_prime(num):
    num_str = str(num)
    for i in range(len(num_str)):
        if not is_prime(int(num_str[i:])):
            return False
    return True

def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True