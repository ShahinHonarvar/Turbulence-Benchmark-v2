def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n):
    if n < 10:
        return True
    if n % 10 == 0:
        return False
    return is_prime(n // 10) and is_left_truncatable(n // 10)

def all_left_truncatable_prime(int_tuple):
    x = int_tuple[78]
    prime_list = [i for i in range(2, x) if is_prime(i) and is_left_truncatable(i)]
    return sorted(prime_list, reverse=True)