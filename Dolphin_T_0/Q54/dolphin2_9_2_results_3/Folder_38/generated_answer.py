def all_right_truncatable_prime(tup):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def right_truncatable(n):
        if n <= 1:
            return False
        if is_prime(n):
            return True
        last_digit = n % 10
        n = n // 10
        return right_truncatable(n)
    x = tup[28]
    lst = []
    for i in range(2, x):
        if right_truncatable(i):
            lst.append(i)
    return sorted(lst)