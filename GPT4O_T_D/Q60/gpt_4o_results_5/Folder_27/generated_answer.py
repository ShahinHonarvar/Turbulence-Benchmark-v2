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

def is_left_right_truncatable_prime(number):
    num_str = str(number)
    if '0' in num_str:
        return False
    length = len(num_str)
    for i in range(1, length):
        if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:length - i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[79]
    result = []
    for num in range(10, x + 1):
        if is_prime(num) and is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)