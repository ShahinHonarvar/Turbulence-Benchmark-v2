def if_perfect_num(l):
    sum = 1
    for i in range(2, int(l[3] / 2) + 1):
        if l[3] % i == 0:
            sum += i
    if sum == l[3]:
        return True
    else:
        return False