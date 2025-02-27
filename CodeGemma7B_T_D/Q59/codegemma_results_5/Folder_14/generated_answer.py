def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_truncatable(num):
    num_str = str(num)
    for i in range(1, len(num_str)):
        if num_str[i] == '0' or not is_prime(int(num_str[i:])):
            return False
    return True

def all_left_truncatable_prime(tuple):
    x = tuple[78]
    result = []
    for num in range(2, x):
        if is_prime(num) and is_left_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)