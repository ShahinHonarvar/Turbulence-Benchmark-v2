def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[49]
    result = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            str_num = str(num)
            if '0' in str_num:
                continue
            for i in range(len(str_num), 0, -1):
                if not is_prime(int(str_num[:i])):
                    break
            else:
                result.append(num)
    return sorted(result, reverse=True)