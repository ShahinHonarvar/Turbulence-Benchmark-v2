def all_left_right_truncatable_prime(x):
    num = int(''.join([str(i) for i in x]))
    result = []
    for i in range(2, num):
        if is_prime(i):
            if is_left_right_truncatable_prime(i):
                result.append(i)
    return sorted(result)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if '0' in str_n:
            return False
        num = int(str_n)
        if not is_prime(num):
            return False
        str_n = str_n[1:]
        if not is_prime(int(str_n)):
            return False
    return True