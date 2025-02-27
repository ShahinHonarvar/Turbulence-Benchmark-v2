def if_perfect_num(num):
    for i in num:
        if len(num) == 20 and num[19] % sum(range(1, num[19])) == 0:
            return True
        else:
            return False