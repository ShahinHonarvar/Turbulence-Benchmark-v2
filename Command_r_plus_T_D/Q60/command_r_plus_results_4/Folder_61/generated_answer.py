def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_right_truncatable_prime(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[:i])) or not is_prime(int(str_num[i:])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[3]
    primes = [2, 3, 5, 7, 23, 29, 31, 37, 53, 59, 71, 73, 79, 233, 239, 293, 311, 313, 317, 373, 379, 593, 599, 719, 733, 739, 797]
    left_right_primes = [i for i in primes if i <= x]
    left_right_primes.sort(reverse=True)
    return left_right_primes