def is_right_truncatable_prime(n):
    if not all((n % i != 0 for i in range(2, int(n ** 0.5) + 1))):
        return False
    m = n
    while m > 0:
        m //= 10
        if not all((m % i != 0 for i in range(2, int(m ** 0.5) + 1))) or (m == 1 and n > 2):
            return False
    return True

def all_right_truncatable_prime(num_tuple):
    if len(num_tuple) < 20:
        return []
    x = num_tuple[19]
    return sorted([i for i in range(2, x) if is_right_truncatable_prime(i)], reverse=True)