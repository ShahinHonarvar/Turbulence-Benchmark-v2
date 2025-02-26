def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[49]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        is_left_right_truncatable = True
        current_num = num
        while current_num > 0:
            if not is_prime(current_num):
                is_left_right_truncatable = False
                break
            current_num //= 10
        current_num = num
        num_str = str(current_num)
        while len(num_str) > 1:
            num_str = num_str[1:]
            current_num = int(num_str)
            if not is_prime(current_num):
                is_left_right_truncatable = False
                break
        if is_left_right_truncatable:
            result.append(num)
    return sorted(result)