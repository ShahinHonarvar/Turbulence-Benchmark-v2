def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    str_num = str(num)
    if '0' in str_num:
        return False
    length = len(str_num)
    for i in range(length):
        if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:length - i])):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[69]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes