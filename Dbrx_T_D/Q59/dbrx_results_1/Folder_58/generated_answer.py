def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 10:
        n //= 10
        if not is_prime(n):
            return False
    return True

def all_left_truncatable_prime(t):
    pos_ints = [i for i in range(t[974] + 1) if left_truncatable_prime(i)]
    pos_ints.sort(reverse=True)
    return pos_ints