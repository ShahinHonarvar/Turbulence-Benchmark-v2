def all_left_truncatable_prime(t):

    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    def is_left_truncatable_prime(x):
        if '0' in str(x):
            return False
        for i in range(1, len(str(x))):
            if not is_prime(int(str(x)[:i])):
                return False
        return True
    x = t[945]
    result = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)