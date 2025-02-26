def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[10]
    result = []
    for num in range(x - 1, 1, -1):
        if '0' in str(num):
            continue
        is_left_truncatable = True
        truncated_num = num
        while truncated_num > 0:
            if not is_prime(truncated_num):
                is_left_truncatable = False
                break
            truncated_num = int(str(truncated_num)[1:] or 0)
        if is_left_truncatable:
            result.append(num)
    return sorted(result, reverse=True)