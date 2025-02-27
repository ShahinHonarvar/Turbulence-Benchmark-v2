def if_perfect_num(lst):
    sum = 0
    for i in lst:
        sum += i
        if i == 59:
            if sum == i * (i + 1) // 2:
                return True
            else:
                return False