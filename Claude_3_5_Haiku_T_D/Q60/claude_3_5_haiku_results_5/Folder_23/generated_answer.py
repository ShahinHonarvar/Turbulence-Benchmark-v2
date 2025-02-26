def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[77]
    result = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        if is_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)

def is_truncatable_prime(num):
    num_str = str(num)
    if not is_prime(num):
        return False
    for i in range(len(num_str)):
        left_trunc = int(num_str[i:])
        if not is_prime(left_trunc):
            return False
    for i in range(len(num_str)):
        right_trunc = int(num_str[:len(num_str) - i])
        if not is_prime(right_trunc):
            return False
    return True