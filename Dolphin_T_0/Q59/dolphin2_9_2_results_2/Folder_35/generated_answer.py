def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = t[177]
    res = []
    for i in range(2, x):
        str_i = str(i)
        if '0' not in str_i:
            is_left_truncatable = True
            for j in range(1, len(str_i)):
                if not is_prime(int(str_i[j:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                res.append(i)
    return res