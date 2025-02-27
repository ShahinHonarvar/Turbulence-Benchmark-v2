def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable(n):
        n_str = str(n)
        return all((is_prime(int(n_str[i:])) for i in range(len(n_str)))) and n_str.count('0') == 0
    x = t[52]
    return sorted([n for n in range(2, x) if left_truncatable(n)], reverse=True)