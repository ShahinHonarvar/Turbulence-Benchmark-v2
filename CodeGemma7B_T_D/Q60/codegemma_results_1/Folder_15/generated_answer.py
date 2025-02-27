def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    str_n = str(n)
    for i in range(len(str_n) - 1):
        if str_n[i] == '0' or not is_prime(int(str_n[i + 1:])):
            return False
    return is_prime(int(str_n))

def is_right_truncatable_prime(n):
    str_n = str(n)
    for i in range(len(str_n) - 1):
        if str_n[i] == '0' or not is_prime(int(str_n[:len(str_n) - i - 1])):
            return False
    return is_prime(int(str_n))

def all_left_right_truncatable_prime(tup):
    x = tup[6]
    result = []
    for n in range(x, 2, -1):
        if is_left_truncatable_prime(n) and is_right_truncatable_prime(n):
            result.append(n)
    return sorted(result, reverse=True)