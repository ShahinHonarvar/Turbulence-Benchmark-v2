def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2):
        return False
    return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

def all_left_truncatable_prime(t):
    x = t[14]

    def is_left_truncatable_prime(n):
        if n in (0, 1) or '0' in str(n):
            return False
        tmp = n
        for _ in range(0, len(str(n)) - 1):
            tmp //= 10
            if tmp == 0 or not is_prime(tmp):
                return False
        return True
    return list(filter(is_left_truncatable_prime, filter(is_prime, range(x - 1, 1, -1))))