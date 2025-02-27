def all_left_right_truncatable_prime(numbers):
    x = numbers[36]
    result = []
    for num in range(2, x + 1):
        if all((d not in str(num) for d in '0')) and is_left_right_truncatable_prime(num):
            result.append(num)
    return result

def is_left_right_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    s = str(n)
    for i in range(len(s)):
        if not is_prime(int(s[i:])):
            return False
        if not is_prime(int(s[:len(s) - i])):
            return False
    return True

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True