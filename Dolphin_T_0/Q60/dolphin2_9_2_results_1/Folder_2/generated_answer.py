def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = t[618]
    res = []
    for num in range(2, x + 1):
        if is_prime(num):
            str_num = str(num)
            left_right = len(str_num)
            while left_right > 1:
                left = str_num[1:left_right]
                right = str_num[0:left_right - 1]
                if not is_prime(int(left)) or not is_prime(int(right)):
                    break
                left_right -= 1
            else:
                res.append(num)
    return sorted(res)