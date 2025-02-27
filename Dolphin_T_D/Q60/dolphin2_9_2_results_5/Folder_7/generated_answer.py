def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n)) - 1, 0, -1):
            if int(str(n)[1:i]) != 0 and str(n)[0] + str(n)[i:len(str(n)) - 1] != 0 and is_prime(int(str(n)[1:i])) and is_prime(int(str(n)[i:len(str(n)) - 1])):
                return True
        return False
    x = t[803]
    return sorted(list(filter(lambda a: is_truncatable_prime(a), range(2, x + 1))), key=lambda b: b)