def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n):
    if n == 0:
        return False
    str_n = str(n)
    while str_n:
        if not is_prime(int(str_n)):
            return False
        str_n = str_n[:-1]
    return True

def all_right_truncatable_prime(numbers):
    if len(numbers) <= 760:
        return []
    x = numbers[760]
    result = []
    for i in range(2, x):
        if right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)