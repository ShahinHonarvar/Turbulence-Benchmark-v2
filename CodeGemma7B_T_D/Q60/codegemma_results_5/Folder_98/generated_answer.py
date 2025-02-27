def all_left_right_truncatable_prime(t):
    x = t[8]

    def is_prime(x):
        if x < 2:
            return False
        for k in range(2, int(x ** 0.5) + 1):
            if x % k == 0:
                return False
        return True
    result = []
    for n in reversed(range(2, x + 1)):
        if not '0' in str(n) and is_prime(n):
            for k in range(1, len(str(n))):
                if not is_prime(int(str(n)[:-k])):
                    break
            else:
                result.append(n)
    return result