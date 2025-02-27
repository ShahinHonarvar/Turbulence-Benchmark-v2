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
    s = str(n)
    while len(s) > 1:
        s = s[1:-1]
        if not s or (s and s != '0' and is_prime(int(s))):
            continue
        else:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[92]
    result = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_prime(num) and is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)