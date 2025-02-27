def all_left_right_truncatable_prime(arg):

    def is_trunc_prime(n):
        s = str(n)
        return all((int(s[i:j]) == s[i:j] and is_prime(int(s[i:j])) for i in range(len(s)) for j in range(i + 1, len(s) + 1)))

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n < 2:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    x = arg[49]
    return sorted([i for i in range(x, 1, -1) if is_trunc_prime(i)], reverse=True)