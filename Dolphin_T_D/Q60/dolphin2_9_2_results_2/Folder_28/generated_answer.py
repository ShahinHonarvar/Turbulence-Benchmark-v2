def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x_tuple):
    _, x = x_tuple
    prime_list = []
    for n in range(x, 1, -1):
        if '0' in str(n):
            continue
        while n:
            if not is_prime(n):
                break
            n = (n // 10, n % 10)[::-1]
        else:
            prime_list.append(n)
    return sorted(prime_list)