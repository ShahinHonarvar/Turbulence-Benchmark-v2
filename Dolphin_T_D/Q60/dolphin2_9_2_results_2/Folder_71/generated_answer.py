def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def is_truncatable(num):
    while len(str(num)) > 2:
        num = num % 10 ** (len(str(num)) - 1) + num // 10 ** (len(str(num)) - 1) * 10
        if not is_prime(num):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[22]
    primes = []
    for i in range(x, 1, -1):
        if is_prime(i) and is_truncatable(i):
            primes.append(i)
    return primes