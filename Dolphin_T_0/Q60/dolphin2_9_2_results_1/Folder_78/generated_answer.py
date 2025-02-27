def all_left_right_truncatable_prime(x):

    def is_prime(n: int) -> bool:
        if n <= 1 or (n % 2 == 0 and n > 2):
            return False
        return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

    def is_truncatable(n: int) -> bool:
        ss = str(n)
        if ss == '0':
            return False
        while len(ss) >= 2:
            if not is_prime(int(ss[1:]) if ss != '0' else int(ss)):
                return False
            ss = ss[1:]
        return True
    return sorted([n for n in range(1, x + 1) if is_prime(n) and is_truncatable(n)])