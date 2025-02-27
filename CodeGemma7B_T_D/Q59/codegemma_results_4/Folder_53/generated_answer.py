def all_left_truncatable_prime(tup):
    x = tup[86]
    answer = []

    def isprime(n):
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

    def check(num):
        str_num = str(num)
        list_num = list(str_num)
        if '0' in list_num:
            return False
        if isprime(num):
            for i in range(1, len(list_num)):
                str_num = ''.join(list_num[i:])
                if not isprime(int(str_num)):
                    return False
            answer.append(num)
            return True
        return False
    for i in range(1, x):
        check(i)
    answer.sort(reverse=True)
    return answer