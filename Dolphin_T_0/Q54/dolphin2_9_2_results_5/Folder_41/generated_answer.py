def all_right_truncatable_prime(x):

    def is_pr(n):
        if n == 0:
            return False
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    n = 1
    L = []
    while n < x:
        if all(is_pr(int(n))):
            L.append(n)
        n += 1
    L.sort(reverse=True)
    return L