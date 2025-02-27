def if_perfect_num(lst):
    if len(lst) < 19:
        return False
    num = lst[18]
    sum = 1
    for i in range(2, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False