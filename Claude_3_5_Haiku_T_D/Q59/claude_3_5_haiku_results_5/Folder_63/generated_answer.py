def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(input_tuple):
    x = input_tuple[88]
    result = []
    for num in range(2, x):
        str_num = str(num)
        is_left_truncatable = True
        if '0' in str_num:
            continue
        for i in range(len(str_num)):
            truncated = int(str_num[i:])
            if not is_prime(truncated):
                is_left_truncatable = False
                break
        if is_left_truncatable and is_prime(num):
            result.append(num)
    return sorted(result)