def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[41]
    result = []
    for num in range(x - 1, 1, -1):
        if '0' in str(num):
            continue
        is_left_truncatable = True
        str_num = str(num)
        while len(str_num) > 1:
            str_num = str_num[1:]
            if not is_prime(int(str_num)):
                is_left_truncatable = False
                break
        if is_left_truncatable and is_prime(num):
            result.append(num)
    return sorted(result, reverse=True)