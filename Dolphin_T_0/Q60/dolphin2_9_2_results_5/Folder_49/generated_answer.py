def all_left_right_truncatable_prime(t):

    def check_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def check_truncatable(num):
        if num < 10:
            return False
        num_0 = str(num)
        for i in range(len(num_0)):
            if num_0[i] == '0':
                return False
        for i in range(len(num_0)):
            if not check_prime(int(num_0[i:])) or not check_prime(int(num_0[:i])):
                return False
        return True
    x = t[14]
    return sorted((i for i in range(1, x + 1) if check_truncatable(i)))