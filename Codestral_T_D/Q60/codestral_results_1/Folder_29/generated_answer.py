def all_left_right_truncatable_prime(numbers):
    x = numbers[55]
    primes = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_left_right_truncatable_prime(num):
    if '0' in str(num):
        return False
    if not is_prime(num):
        return False
    while num > 0:
        num = int(str(num)[1:])
        if num != 0 and num != 1 and (not is_prime(num)):
            return False
        num = int(str(num)[:-1])
        if num != 0 and num != 1 and (not is_prime(num)):
            return False
    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True