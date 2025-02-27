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

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    s = str(n)
    while len(s) > 2:
        s = s[1:-1]
        if not is_prime(int(s)):
            return False
    return len(s) == 1 or is_prime(int(s))

def all_left_right_truncatable_prime(numbers):
    x = numbers[92]
    result = []
    for i in range(10, x + 1):
        if is_prime(i) and is_truncatable_prime(i):
            result.append(i)
    return result