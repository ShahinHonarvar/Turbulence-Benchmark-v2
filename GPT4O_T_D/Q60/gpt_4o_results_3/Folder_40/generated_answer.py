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
    num_str = str(n)
    if '0' in num_str:
        return False
    while len(num_str) > 1:
        num_str = num_str[1:-1]
        if num_str and (not is_prime(int(num_str))):
            return False
    return is_prime(n)

def all_left_right_truncatable_prime(numbers):
    x = numbers[10] if len(numbers) > 10 else 0
    result = []
    for n in range(2, x + 1):
        if is_left_right_truncatable_prime(n):
            result.append(n)
    return sorted(result, reverse=True)