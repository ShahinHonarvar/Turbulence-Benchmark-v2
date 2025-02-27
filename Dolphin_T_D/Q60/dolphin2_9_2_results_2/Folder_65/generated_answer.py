def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n == 1:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    x, res = (t[32], [])
    for n in range(2, x + 1):
        if is_prime(n):
            while n > 9:
                n_str = str(n)
                if '0' not in n_str:
                    if is_prime(int(n_str[1:])) and is_prime(int(n_str[:-1])):
                        n = int(n_str[1:])
                        continue
                n = 0
                break
            if n in (2, 3):
                res.append(n)
    return res