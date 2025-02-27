def all_left_right_truncatable_prime(n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(num):
        str_num = str(num)
        while len(str_num) > 2:
            if is_prime(int(str_num[1:-1])):
                str_num = str_num[1:-1]
            else:
                return False
        if len(str_num) > 0:
            if is_prime(int(str_num)):
                return True
            else:
                return False
        else:
            return False
    return sorted([i for i in range(2, n[175] + 1) if is_left_right_truncatable_prime(i)])