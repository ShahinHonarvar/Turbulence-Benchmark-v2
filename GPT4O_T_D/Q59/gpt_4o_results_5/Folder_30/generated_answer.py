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

def is_left_truncatable_prime(num):
    s = str(num)
    for i in range(len(s)):
        if not is_prime(int(s[i:])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[37]
    result = []
    for number in range(2, x):
        if '0' not in str(number) and is_left_truncatable_prime(number):
            result.append(number)
    return sorted(result, reverse=True)