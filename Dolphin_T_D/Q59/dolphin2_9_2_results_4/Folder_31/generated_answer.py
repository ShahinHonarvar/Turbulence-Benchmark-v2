def is_prime(n):
    if n in (0, 1):
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    if len(t) < 51:
        return 'Input has less than 51 elements'
    x = t[50]
    result = []
    for i in range(x - 1, 1, -1):
        str_i = str(i)
        while str_i and is_prime(int(str_i)):
            str_i = str_i[1:]
            if str_i and is_prime(int(str_i)):
                result.append(i)
                break
    return sorted(result, reverse=True)