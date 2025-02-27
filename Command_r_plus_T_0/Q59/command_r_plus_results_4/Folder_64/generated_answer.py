def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_truncatable_prime(num):
    if num < 10 and is_prime(num):
        return True
    str_num = str(num)
    for i in range(1, len(str_num)):
        if str_num[:i].count('0') > 0 or not is_prime(int(str_num[:i])):
            return False
    return is_prime(num)

def all_left_truncatable_prime(numbers):
    x = numbers[4]
    primes = [2, 3, 5, 7]
    for i in range(10, x):
        if left_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)