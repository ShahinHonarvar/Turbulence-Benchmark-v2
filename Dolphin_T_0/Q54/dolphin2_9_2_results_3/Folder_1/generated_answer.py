def all_right_truncatable_prime(T):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n == 1 or n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        n = str(n)
        return all((is_prime(int(n[i:])) for i in range(len(n))))
    x = T[20]
    res = [x for x in range(2, x) if is_right_truncatable_prime(x)]
    return sorted(res, reverse=True)