def if_perfect_num(lst):
    num = lst[83]
    s = 1
    for i in range(2, num):
        if num % i == 0:
            s = s + i
    if s == num and num != 1:
        return True
    else:
        return False