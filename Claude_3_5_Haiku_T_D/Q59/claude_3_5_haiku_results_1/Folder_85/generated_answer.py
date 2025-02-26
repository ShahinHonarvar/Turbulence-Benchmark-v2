def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[94]
    result = []
    for num in range(2, x):
        str_num = str(num)
        is_truncatable = True
        for i in range(len(str_num)):
            truncated_num = int(str_num[i:])
            if not is_prime(truncated_num):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num) and ('0' not in str_num):
            result.append(num)
    return sorted(result)