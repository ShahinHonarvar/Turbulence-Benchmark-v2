def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[67]
    result = []

    def is_left_truncatable_prime(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        while len(str_num) > 0:
            if not is_prime(int(str_num)):
                return False
            str_num = str_num[1:]
        return True
    for n in range(x - 1, 1, -1):
        if is_left_truncatable_prime(n):
            result.append(n)
    return sorted(result, reverse=True)