def sum_in_range(num):
    sum = 0
    for i in num:
        if i >= -816 and i <= -166:
            sum = sum + i
    if sum == 0:
        return 0
    else:
        return sum