def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[54]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        is_truncatable = True
        left_truncate = num
        right_truncate = num
        while left_truncate > 9:
            left_truncate //= 10
            if not is_prime(left_truncate):
                is_truncatable = False
                break
        while right_truncate > 9:
            right_truncate %= 10 ** (len(str(right_truncate)) - 1)
            if not is_prime(right_truncate):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            result.append(num)
    return sorted(result)