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

def is_left_right_truncatable(prime):
    s = str(prime)
    while len(s) > 1:
        s = s[1:-1]
        if not is_prime(int(s)):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[87]
    result = []
    for i in range(11, x + 1):
        if not '0' in str(i) and is_prime(i) and is_left_right_truncatable(i):
            result.append(i)
    return result