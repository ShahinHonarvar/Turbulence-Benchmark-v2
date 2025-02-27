def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    str_n = str(n)
    if '0' in str_n or len(str_n) <= 1:
        return False
    for i in range(1, len(str_n)):
        left = int(str_n[:i])
        right = int(str_n[i:])
        if not (is_prime(left) and is_prime(right)):
            return False
    return True

def all_left_right_truncatable_prime(x):
    prime_list = [i for i in range(2, x + 1) if is_prime(i)]
    truncatable_prime_list = []
    for i in prime_list:
        if is_truncatable(i):
            truncatable_prime_list.append(i)
    truncatable_prime_list.sort(reverse=True)
    return truncatable_prime_list