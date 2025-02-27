def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[86]
    result = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        is_left_truncatable = True
        truncated_num = num
        while truncated_num > 0:
            truncated_num //= 10
            if not is_prime(truncated_num):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            result.append(num)
    result.sort()
    return result