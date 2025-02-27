def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_right_truncatable_prime(n):
    s = str(n)
    for i in range(len(s)):
        if not (is_prime(int(s[i:])) and is_prime(int(s[:len(s) - i]))):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[71]
    result = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)