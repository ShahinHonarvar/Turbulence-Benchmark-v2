def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        while n > 1:
            n = int(n / 10)
            if not is_prime(n):
                return False
        return True
    x = t[92]
    lst = []
    for i in range(2, x):
        if is_right_truncatable(i):
            lst.append(i)
    return sorted(lst)