def all_left_right_truncatable_prime(n):
    result = []
    for i in range(len(n)):
        temp = int(n[i])
        if is_prime(temp):
            if is_truncatable(temp):
                result.append(temp)
    return result

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    str_n = str(n)
    for i in range(1, len(str_n)):
        left = int(str_n[i:])
        right = int(str_n[:-i])
        if not (is_prime(left) and is_prime(right)):
            return False
    return True