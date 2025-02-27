def all_left_right_truncatable_prime(t):
    x = t[29]

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def are_truncatable(s):
        for i in range(len(s) - 1):
            if not is_prime(int(s[i + 1:] + s[i])):
                return False
        return True
    return [int(s) for s in filter(are_truncatable, map(str, range(2, x + 1)))]