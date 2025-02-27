def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def left_truncatable_prime(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True

    def right_truncatable_prime(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[:-i])):
                return False
        return True

    def left_right_truncatable_prime(n):
        lst = []
        for i in range(2, n + 1):
            if is_prime(i) and left_truncatable_prime(i) and right_truncatable_prime(i):
                lst.append(i)
        return lst
    x = int(x)
    return sorted(left_right_truncatable_prime(x), reverse=True) if left_right_truncatable_prime(x) else []