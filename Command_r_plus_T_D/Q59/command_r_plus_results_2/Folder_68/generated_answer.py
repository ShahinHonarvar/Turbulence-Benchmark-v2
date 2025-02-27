def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_truncatable_prime(num):
    if num < 10 and (not is_prime(num)):
        return False
    str_num = str(num)
    for i in range(len(str_num)):
        truncated_num = int(str_num[i:])
        if not is_prime(truncated_num):
            return False
    return True

def all_left_truncatable_prime(numbers):
    limit = numbers[1]
    left_truncatable_primes = []
    for num in range(2, limit):
        if left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)