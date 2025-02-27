def if_perfect_num(l):
    sum = 0
    for i in range(1, l[41]):
        if l[41] % i == 0:
            sum = sum + i
    if sum == l[41]:
        return True
    else:
        return False