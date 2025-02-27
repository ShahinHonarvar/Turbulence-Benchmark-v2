def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(prime):
    str_prime = str(prime)
    length = len(str_prime)
    for i in range(1, length):
        left_trunc = int(str_prime[i:])
        right_trunc = int(str_prime[:length - i])
        if not is_prime(left_trunc) or not is_prime(right_trunc):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[55]
    result = []
    for num in range(11, x + 1):
        if '0' not in str(num) and is_prime(num) and is_left_right_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)