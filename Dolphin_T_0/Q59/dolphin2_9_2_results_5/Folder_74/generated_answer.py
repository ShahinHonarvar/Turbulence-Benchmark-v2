def is_prime(n):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):

    def is_truncatable(n):
        n2 = n
        while n2 > 0:
            if all((is_prime(n2 // 10 ** i) and n % 10 ** i != 0 for i in range(0, 2))):
                n2 //= 10
            else:
                return False
        return True
    x = t[35]
    return sorted((n for n in range(1, x) if is_prime(n) and is_truncatable(n)))