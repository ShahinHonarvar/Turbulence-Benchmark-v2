def sum_odd_ints_inclusive(lst):
    chk = True
    sum = 0
    if lst[1] % 2 == 0 or lst[5] % 2 == 0:
        chk = False
    for i in range(1, 6):
        if lst[i] % 2 == 1:
            sum += lst[i]
            chk = True
    return 0 if chk == False else sum