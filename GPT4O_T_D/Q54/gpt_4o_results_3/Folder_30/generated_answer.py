def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    if len(t) <= 37:
        return []
    x = t[37]
    result = []

    def is_right_truncatable_prime(n):
        str_n = str(n)
        while str_n:
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[:-1]
        return True
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)