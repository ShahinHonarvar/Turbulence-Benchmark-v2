def all_left_truncatable_prime(numbers):
    x = numbers[784]
    result = []
    for i in range(x):
        if is_prime(i) and str(i).count('0') == 0:
            if is_left_truncatable(i):
                result.append(i)
    return result

def is_left_truncatable(n):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True