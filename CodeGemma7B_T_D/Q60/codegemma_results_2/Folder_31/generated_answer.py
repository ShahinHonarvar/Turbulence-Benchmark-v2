def all_left_right_truncatable_prime(tup):
    x = tup[50]
    res = []

    def isprime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(1, len(str_num)):
            if not isprime(int(str_num[i:])):
                return False
        for i in range(1, len(str_num)):
            if not isprime(int(str_num[:-i])):
                return False
        return True
    for i in range(2, (x + 1) // 2):
        if isprime(i) and is_truncatable(i):
            res.append(i)
    res.sort(reverse=True)
    return res