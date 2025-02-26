def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[98]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if not is_prime(num):
            continue
        is_truncatable = True
        temp_num_left = num
        temp_num_right = num
        while temp_num_left > 9:
            temp_num_left //= 10
            if not is_prime(temp_num_left):
                is_truncatable = False
                break
        while temp_num_right > 9:
            temp_num_right %= 10 ** (len(str(temp_num_right)) - 1)
            if not is_prime(temp_num_right):
                is_truncatable = False
                break
        if is_truncatable:
            result.append(num)
    return sorted(result)