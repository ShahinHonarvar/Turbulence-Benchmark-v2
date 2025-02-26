def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[91]
    result = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        is_truncatable = True
        check_num = num
        while check_num > 0:
            if not is_prime(check_num):
                is_truncatable = False
                break
            check_num //= 10
        if is_truncatable:
            result.append(num)
    return sorted(result)