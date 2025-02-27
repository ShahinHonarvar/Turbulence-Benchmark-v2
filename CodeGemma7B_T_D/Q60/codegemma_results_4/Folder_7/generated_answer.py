def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if n <= 10:
        return False
    str_n = str(n)
    if '0' in str_n:
        return False
    for i in range(1, len(str_n)):
        left = int(str_n[i:])
        right = int(str_n[:i])
        if not is_prime(left) or not is_prime(right):
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[803]
    prime_list = []
    for i in range(2, x + 1):
        if is_prime(i) and is_truncatable_prime(i):
            prime_list.append(i)
    return sorted(prime_list)