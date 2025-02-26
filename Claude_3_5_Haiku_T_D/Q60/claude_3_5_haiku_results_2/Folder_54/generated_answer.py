def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    digits = str(n)
    for i in range(len(digits)):
        trunc_num = int(digits[i:])
        if not is_prime(trunc_num):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[88]
    result = []
    for num in range(x, 11, -1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return result