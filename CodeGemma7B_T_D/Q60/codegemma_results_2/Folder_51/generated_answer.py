def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    str_n = str(n)
    if '0' in str_n or len(str_n) == 1:
        return False
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
    return True

def right_truncatable_prime(n):
    str_n = str(n)
    if '0' in str_n or len(str_n) == 1:
        return False
    for i in range(len(str_n) - 1, 0, -1):
        if not is_prime(int(str_n[:i])):
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[54]
    prime_list = []
    for i in range(2, x + 1):
        if is_prime(i):
            if left_truncatable_prime(i) and right_truncatable_prime(i):
                prime_list.append(i)
    return sorted(prime_list)