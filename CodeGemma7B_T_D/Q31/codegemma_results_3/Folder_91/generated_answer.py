def if_perfect_num(lst):
    num = lst[6]
    sm = 0
    for i in range(1, num):
        if num % i == 0:
            sm += i
    if sm == num:
        return True
    else:
        return False