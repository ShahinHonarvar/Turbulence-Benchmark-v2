def all_left_right_truncatable_prime(tup):
    x = tup[91]

    def is_prime(n):
        return n > 1 and all((n % i for i in range(2, int(n ** 0.5) + 1)))

    def is_truncatable_prime(n):
        ns = str(n)
        if '0' in ns or len(ns) <= 1:
            return False
        for i in range(1, len(ns)):
            if not is_prime(int(ns[i:])):
                return False
            if not is_prime(int(ns[:-i])):
                return False
        return True
    ans = [i for i in range(2, x + 1) if is_truncatable_prime(i)]
    return sorted(ans) if ans else []