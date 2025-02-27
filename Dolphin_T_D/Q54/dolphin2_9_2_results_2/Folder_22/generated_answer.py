def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        n = str(n)
        for i in range(1, len(n)):
            if not is_prime(int(n[i:])):
                return False
        return True
    x = t[85]
    lst = []
    for i in range(x):
        if is_prime(i) and is_right_truncatable(i):
            lst.append(i)
    return sorted(lst)