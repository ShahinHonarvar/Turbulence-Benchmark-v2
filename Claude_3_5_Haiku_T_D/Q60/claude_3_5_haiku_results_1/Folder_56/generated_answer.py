def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(data):
    x = data[30]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        is_truncatable = True
        current_left = num
        while current_left > 0:
            if not is_prime(current_left):
                is_truncatable = False
                break
            current_left //= 10
        current_right = num
        str_num = str(num)
        while current_right > 0:
            if not is_prime(current_right):
                is_truncatable = False
                break
            str_num = str_num[:-1]
            current_right = int(str_num) if str_num else 0
        if is_truncatable:
            result.append(num)
    return sorted(result)