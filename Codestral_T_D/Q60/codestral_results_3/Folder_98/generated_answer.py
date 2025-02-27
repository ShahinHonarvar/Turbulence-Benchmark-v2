def all_left_right_truncatable_prime(t):
    x = t[8]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate(n):
        s = str(n)
        return [int(s[i:]) for i in range(len(s))] + [int(s[:i]) for i in range(1, len(s))]
    result = []
    for i in range(2, x + 1):
        if '0' in str(i):
            continue
        if all((is_prime(j) for j in truncate(i))):
            result.append(i)
    return sorted(result, reverse=True)