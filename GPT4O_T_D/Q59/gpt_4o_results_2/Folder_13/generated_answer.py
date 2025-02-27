def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    n = str(n)
    while n:
        if not is_prime(int(n)):
            return False
        n = n[1:]
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[784]
    result = []
    for number in range(2, x):
        if '0' not in str(number) and is_left_truncatable_prime(number):
            result.append(number)
    return result