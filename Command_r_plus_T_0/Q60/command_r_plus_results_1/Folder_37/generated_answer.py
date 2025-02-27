def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_right_truncatable_prime(num):
    str_num = str(num)
    for i in range(len(str_num)):
        if not is_prime(int(str_num[:i] + str_num[i + 1:])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    max_val = numbers[35]
    truncatable_primes = []
    for num in range(max_val, 1, -1):
        if left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)