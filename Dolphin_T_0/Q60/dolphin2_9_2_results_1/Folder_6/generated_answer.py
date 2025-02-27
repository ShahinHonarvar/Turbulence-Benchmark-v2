def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n) - 1):
            if str_n[0] == '0' or str_n[-1] == '0':
                return False
            if not is_prime(int(str_n[i + 1:])) or not is_prime(int(str_n[:i + 1])):
                return False
        return True
    x = t[74]
    lst = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            lst.append(i)
    lst.sort()
    return lst