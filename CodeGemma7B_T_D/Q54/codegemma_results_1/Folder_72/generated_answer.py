def all_right_truncatable_prime(n):
    x = n[31]
    result = []
    for num in range(x - 1, 0, -1):
        if is_prime(num) and is_right_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_right_truncatable(num):
    num_str = str(num)
    for i in range(1, len(num_str)):
        truncated_num = int(num_str[:-i])
        if not is_prime(truncated_num):
            return False
    return True