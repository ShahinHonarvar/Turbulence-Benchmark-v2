def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2 or n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if str_n[i] == '0' or not is_prime(int(str_n[i:])):
                return False
        return True
    m = t[3]
    result = []
    for n in range(m, 0, -1):
        if is_prime(n) and is_truncatable(n):
            result.append(n)
    return result