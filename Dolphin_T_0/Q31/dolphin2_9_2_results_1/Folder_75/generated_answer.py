def if_perfect_num(l):
    i = l[80]
    div_sum = 0
    for k in range(1, i):
        if i % k == 0:
            div_sum += k
    return div_sum == i