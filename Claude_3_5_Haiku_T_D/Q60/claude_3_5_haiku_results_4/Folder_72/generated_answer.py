def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[31]
    result = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_truncatable = True
        temp_num = num
        while temp_num > 0:
            if not is_prime(temp_num):
                is_truncatable = False
                break
            temp_num //= 10
        temp_num = num
        digit_len = len(str(num))
        while digit_len > 1:
            temp_num %= 10 ** (digit_len - 1)
            if not is_prime(temp_num):
                is_truncatable = False
                break
            digit_len -= 1
        if is_truncatable:
            result.append(num)
    return result