def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_truncatable(num):
    str_num = str(num)
    for i in range(len(str_num)):
        if not is_prime(int(str_num[i:])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    if len(numbers) <= 69:
        return []
    x = numbers[69]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num) and is_left_truncatable(num):
            left_truncatable_primes.append(num)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes