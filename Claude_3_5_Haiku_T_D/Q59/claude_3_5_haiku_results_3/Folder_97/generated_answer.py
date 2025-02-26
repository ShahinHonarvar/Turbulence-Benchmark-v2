def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[645]
    result = []
    for n in range(2, x):
        str_n = str(n)
        if '0' in str_n:
            continue
        is_left_truncatable = True
        for i in range(len(str_n)):
            current_num = int(str_n[i:])
            if not is_prime(current_num):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            result.append(n)
    return sorted(result)