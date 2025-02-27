def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n):
    while n != 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(args):
    x = args[78]
    res = [i for i in range(x, 0, -1) if right_truncatable_prime(i)]
    return res