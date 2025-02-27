def all_left_truncatable_prime(x_tuple):
    x = x_tuple[87]
    prime_list = []
    for num in range(2, x):
        if is_prime(num) and is_truncatable(num):
            prime_list.append(num)
    prime_list.sort()
    return prime_list

def is_prime(n):
    for num in range(2, int(n ** 0.5) + 1):
        if n % num == 0:
            return False
    return True

def is_truncatable(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if str_n[i] == '0':
            return False
        n = int(str_n[i:])
        if not is_prime(n):
            return False
    return True