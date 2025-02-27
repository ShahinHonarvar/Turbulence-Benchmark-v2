def if_perfect_num(lst):
    num = lst[34]
    s = 0
    for i in range(1, num):
        if num % i == 0:
            s += i
    return s == num