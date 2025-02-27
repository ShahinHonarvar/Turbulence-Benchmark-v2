def all_left_truncatable_prime(x):
    p = list(range(2, x)) + [x]

    def is_prime(n):
        if n < 1:
            return False
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def remove_left_digits(n):
        l = str(n)
        for i in range(1, len(l)):
            if l[i - 1] != '9':
                l = l[i:]
                break
        if l:
            return int(''.join(l))

    def right_truncatable_prime(n):
        if is_prime(n):
            for d in range(2, n // 2 + 1):
                if remove_left_digits(n - d) == n:
                    return True
            return False

    def left_truncatable_prime(n):
        if is_prime(n):
            for d in range(2, n // 2 + 1):
                if remove_left_digits(d) == n:
                    return True
            return False
    res = []
    for n in p:
        if left_truncatable_prime(n):
            res.append(n)
    return sorted(res)[::-1]