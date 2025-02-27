def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(p):
    if p < 10:
        return is_prime(p) and is_prime(p % 10)
    else:
        return is_prime(p) and is_left_right_truncatable_prime(p // 10)

def all_left_right_truncatable_prime(x):
    prime_list = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            prime_list.append(i)
    return sorted(prime_list)