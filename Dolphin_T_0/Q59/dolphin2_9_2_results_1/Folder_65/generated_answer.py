def all_left_truncatable_prime(n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = n[32]
    res = []
    for num in range(2, x):
        str_num = str(num)
        if '0' not in str_num:
            left_num = str_num
            while left_num[0] != '':
                if not is_prime(int(left_num)):
                    break
                if left_num[0] == '':
                    res.append(int(left_num))
                left_num = left_num[1:]
    return sorted(res)