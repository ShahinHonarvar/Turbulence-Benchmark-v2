def all_left_truncatable_prime(a):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if n < 2:
            return False
        for _ in range(9):
            n //= 10
            if is_prime(n):
                continue
            else:
                return False
        return True
    x = a[int(a[0])]
    l = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    l.sort(reverse=True)
    return l