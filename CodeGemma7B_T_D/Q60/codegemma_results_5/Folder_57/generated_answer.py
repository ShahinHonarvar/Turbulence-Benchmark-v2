def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    for i in range(1, len(str_n)):
        if not (is_prime(int(str_n[i:])) and is_prime(int(str_n[:-i]))):
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[54]
    result = []
    for i in range(x, 2, -1):
        if is_truncatable(i) and is_prime(i):
            result.append(i)
    return sorted(result, reverse=True)