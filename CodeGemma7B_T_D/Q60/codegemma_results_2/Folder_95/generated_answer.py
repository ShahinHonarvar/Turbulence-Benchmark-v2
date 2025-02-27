def all_left_right_truncatable_prime(tpl):
    x = tpl[77]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(1, len(str_n)):
            left = int(str_n[i:])
            right = int(str_n[:-i])
            if not (is_prime(left) and is_prime(right)):
                return False
        return True
    result = [n for n in range(2, x + 1) if is_truncatable_prime(n)]
    return sorted(result) if result else []