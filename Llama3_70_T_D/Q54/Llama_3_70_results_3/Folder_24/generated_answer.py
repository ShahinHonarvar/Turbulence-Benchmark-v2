def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[:len(str_n) - i])):
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[65]
    return sorted([n for n in range(2, x) if is_prime(n) and is_right_truncatable_prime(n)], reverse=True)