def all_right_truncatable_prime(t):

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        n = str(n)
        for i in range(1, len(n)):
            if not is_prime(int(n[n.index(n[-i - 1]):]) and is_prime(int(n[:n.rindex(n[-i - 1])]))):
                return False
        return True
    l = []
    for i in range(t[7]):
        if is_right_truncatable_prime(i):
            l.append(i)
    l.sort()
    return l