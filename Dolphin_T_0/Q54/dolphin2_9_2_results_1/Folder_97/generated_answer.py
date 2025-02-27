def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n == 1:
            return False
        m = int(n ** 0.5) + 1
        for x in range(3, m, 2):
            if n % x == 0:
                return False
        return True

    def is_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = int(str(n)[1:])
        return True
    x = t[645]
    lst = [i for i in range(2, x) if is_prime(i) and is_right_truncatable(i)]
    return sorted(lst)