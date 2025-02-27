def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    left_right_truncatable = []
    for num in range(t[618] + 1):
        if is_prime(num):
            str_num = str(num)
            while len(str_num) > 1 and (str_num.startswith('0') or str_num.endswith('0')):
                if not is_prime(int(str_num[1:])) or not is_prime(int(str_num[:-1])):
                    break
                str_num = str_num[1:-1]
            else:
                if not is_prime(int(str_num[1:])) or not is_prime(int(str_num[:-1])):
                    continue
                left_right_truncatable.append(num)
    return sorted(left_right_truncatable)