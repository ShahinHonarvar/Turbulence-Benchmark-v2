def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        strn = str(n)
        for i in range(len(strn) - 1, 0, -1):
            if not is_prime(int(strn[:i])):
                return False
        return True
    x = t[429]
    r_list = [i for i in range(3, x) if is_truncatable(i) and is_prime(i)]
    r_list.sort(reverse=True)
    return r_list if r_list else []