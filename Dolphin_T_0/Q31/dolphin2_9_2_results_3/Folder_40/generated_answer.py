def if_perfect_num(lst):
    if len(lst) < 8:
        return False
    else:
        num = lst[7]
        perfect = 0
        for i in range(1, num):
            if num % i == 0:
                perfect += i
        return perfect == num