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

def left_right_truncatable(prime):
    if '0' in str(prime):
        return False
    str_prime = str(prime)
    while len(str_prime) > 2:
        str_prime = str_prime[1:-1]
        if not is_prime(int(str_prime)):
            return False
    return len(str_prime) == 2 or len(str_prime) == 1

def all_left_right_truncatable_prime(numbers):
    x = numbers[22]
    result = []
    for num in range(2, x + 1):
        if is_prime(num) and left_right_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)