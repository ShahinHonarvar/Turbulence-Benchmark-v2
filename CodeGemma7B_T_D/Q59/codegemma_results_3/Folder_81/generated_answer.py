def all_left_truncatable_prime(a):

    def is_prime(x):
        if x < 2:
            return False
        if x % 2 == 0:
            return x == 2
        for i in range(3, int(x ** 0.5) + 2, 2):
            if x % i == 0:
                return False
        return True

    def is_truncatable_prime(x):
        if '0' in str(x):
            return False
        for i in range(len(str(x))):
            if not is_prime(int(str(x)[0:len(str(x)) - i])):
                return False
        return True
    s = sorted([x for x in a if is_truncatable_prime(x)])
    return s