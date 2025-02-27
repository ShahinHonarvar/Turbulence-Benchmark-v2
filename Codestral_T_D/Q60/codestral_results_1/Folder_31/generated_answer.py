def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate(n):
        return [int(str(n)[:i]) for i in range(1, len(str(n))) if str(n)[:i].count('0') == 0] + [int(str(n)[i:]) for i in range(1, len(str(n))) if str(n)[i:].count('0') == 0]
    x = t[50]
    result = []
    for i in range(2, x + 1):
        if is_prime(i) and all((is_prime(t) for t in truncate(i))):
            result.append(i)
    return sorted(result, reverse=True)