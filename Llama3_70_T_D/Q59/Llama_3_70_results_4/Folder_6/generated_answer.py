def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(num):
    if not is_prime(num):
        return False
    num_str = str(num)
    if '0' in num_str:
        return False
    while len(num_str) > 1:
        num_str = num_str[1:]
        if not is_prime(int(num_str)):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[74]
    result = [num for num in range(2, x) if left_truncatable_prime(num)]
    result.sort()
    return result