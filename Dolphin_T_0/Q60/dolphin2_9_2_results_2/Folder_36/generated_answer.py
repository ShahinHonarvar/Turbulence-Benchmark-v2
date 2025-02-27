def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def truncate_number(n):
    return [n // 10 ** i % 10 for i in range(len(str(n)) - 1)]

def left_and_right_truncatable(n):
    num = [int(str(n)[i:j + 1]) for i in range(len(str(n))) for j in range(i, len(str(n)))]
    return all((is_prime(i) for i in num))

def all_left_right_truncatable_prime(x):
    return [i for i in range(2, x + 1) if is_prime(i) and left_and_right_truncatable(i)]