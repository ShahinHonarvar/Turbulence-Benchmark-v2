def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True

    def is_right_truncatable_prime(n):
        while len(str(n)):
            if not is_prime(n):
                return False
            n = int(str(n)[:-1])
        return True
    x = t[84]
    l = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    l.sort(reverse=True)
    return l