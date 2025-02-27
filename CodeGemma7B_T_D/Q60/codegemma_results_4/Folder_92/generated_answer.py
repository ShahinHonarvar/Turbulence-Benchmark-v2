def all_left_right_truncatable_prime(x):
    result = []
    for y in range(x + 1):
        txt = str(y)
        if txt.find('0') < 0 and txt.isnumeric() and (2 <= int(y) <= x) and all([str(y)[:i] and str(y)[-i:] not in ['0', '1', '2', '5', '8'] for i in range(1, len(txt) + 1)]) and all([int(str(y)[:i]) and int(str(y)[-i:]) not in prefixs[i] for i in range(1, len(txt) + 1)]) and all([chk_prime(int(str(y)[:i])) and chk_prime(int(str(y)[-i:])) for i in range(1, len(txt) + 1)]) and chk_prime(y):
            result.append(y)
    return sorted(result)

def chk_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True