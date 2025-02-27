def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p ** 2 <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def all_left_truncatable_prime(int_tuple):
    x = int_tuple[28]
    left_truncatable_prime = []
    for i in range(2, x):
        if is_prime(i) and '0' not in str(i):
            trunc_str = str(i)
            while trunc_str:
                if not is_prime(int(trunc_str)):
                    break
                trunc_str = trunc_str[1:]
                if trunc_str and is_prime(int(trunc_str)):
                    left_truncatable_prime.append(i)
                    break
    return sorted(list(set(left_truncatable_prime)))