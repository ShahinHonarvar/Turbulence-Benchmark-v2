def is_prime(num):
    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def right_truncatable_prime(num):
    if not is_prime(num):
        return False
    while num > 0:
        if not is_prime(num):
            return False
        num //= 10
    return True

def all_right_truncatable_prime(numbers):
    result = []
    if len(numbers) > 94:
        x = numbers[94]
        for i in range(2, x):
            if right_truncatable_prime(i):
                result.append(i)
    return sorted(result)