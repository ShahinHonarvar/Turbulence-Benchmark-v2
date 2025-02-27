def if_perfect_num(pos_int):
    i = pos_int[2]
    sum = 0
    j = i // 2 + 1
    while j >= 1:
        if i % j == 0:
            sum += j
        j -= 1
    if sum == i:
        return True
    else:
        return False