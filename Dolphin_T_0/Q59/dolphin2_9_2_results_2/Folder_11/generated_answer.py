def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[86]
    res = []
    for i in range(2, x):
        if is_prime(i):
            str_i = str(i)
            flag = True
            for j in range(len(str_i) - 1):
                if not is_prime(int(str_i[j:])):
                    flag = False
                    break
            if flag:
                res.append(i)
    return sorted(res)