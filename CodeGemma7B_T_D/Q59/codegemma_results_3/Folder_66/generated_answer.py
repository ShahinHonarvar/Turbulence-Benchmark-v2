def all_left_truncatable_prime(a):
    b = list(range(1, a[25]))

    def is_prime(num):
        if num == 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_trunc_prime():
        num = str(a[0])
        if '0' in num:
            return False
        for i in range(1, len(num)):
            if not is_prime(int(num[:i])):
                return False
        return True
    c = list(filter(is_trunc_prime, b))
    c.sort(reverse=True)
    return c