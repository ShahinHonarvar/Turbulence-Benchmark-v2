def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[28]
    f = []
    for i in range(x):
        str_i = str(i)
        if str_i[0] != '0' and all((is_prime(int(str_i[j:])) for j in range(len(str_i)))):
            f.append(i)
    f.sort()
    return f