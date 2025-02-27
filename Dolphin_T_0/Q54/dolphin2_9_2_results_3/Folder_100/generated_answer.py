def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(args):
    x = args[26]
    res = []
    for n in range(2, x):
        while n:
            if is_prime(n):
                res.append(n)
            n //= 10
    return sorted(res)