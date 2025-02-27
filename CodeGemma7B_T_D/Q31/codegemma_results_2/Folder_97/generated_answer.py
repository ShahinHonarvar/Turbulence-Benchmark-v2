def if_perfect_num(list1):
    k = list1[132]
    i = 2
    sum = 0
    while i < k:
        if k % i == 0:
            sum = sum + i
        i = i + 1
    if k == sum:
        return True
    else:
        return False