def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    s = str(n)
    for i in range(len(s)):
        if not is_prime(int(s[i:])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[73]
    result = []
    for num in range(2, x):
        if '0' not in str(num) and is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)