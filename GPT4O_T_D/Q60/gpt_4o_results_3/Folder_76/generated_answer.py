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
    if '0' in str(n):
        return False
    num_str = str(n)
    for i in range(len(num_str)):
        left_truncate = int(num_str[i:])
        right_truncate = int(num_str[:len(num_str) - i])
        if not is_prime(left_truncate) or not is_prime(right_truncate):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) < 371:
        return []
    x = numbers[370]
    result = []
    for number in range(2, x + 1):
        if is_left_right_truncatable_prime(number):
            result.append(number)
    result.sort(reverse=True)
    return result