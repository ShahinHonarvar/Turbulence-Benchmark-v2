def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable(n):
    while n >= 10:
        n = int(str(n)[:-1])
        if not is_prime(n):
            return False
    return True

def left_truncatable(n):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
    return True

def all_left_right_truncatable_prime(args):
    x = args[0]
    result = []
    for i in range(2, x + 1):
        if is_prime(i) and right_truncatable(i) and left_truncatable(i) and (str(i).count('0') == 0):
            result.append(i)
    result.sort(reverse=True)
    return result or []