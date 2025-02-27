def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_right_truncatable_prime(n):
    if n < 10 and is_prime(n):
        return True
    if str(n)[0] == '0' or str(n)[-1] == '0':
        return False
    left_part = str(n)[:-1]
    right_part = str(n)[1:]
    return is_prime(int(left_part)) and is_prime(int(right_part)) and is_left_right_truncatable_prime(int(left_part)) and is_left_right_truncatable_prime(int(right_part))

def all_left_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:
    result = []
    for num in numbers:
        if num > 0 and is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)