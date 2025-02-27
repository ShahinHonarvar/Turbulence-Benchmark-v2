def if_perfect_num(x):
    y = x[24]
    p = 1
    sum = 0
    for i in range(2, y // 2 + 1):
        if y % i == 0:
            sum += i
    if sum == y:
        return True
    else:
        return False