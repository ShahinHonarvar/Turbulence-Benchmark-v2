def gcf_two_nums(list):
    x = list[56]
    y = list[54]
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if greater % x == 0 and greater % y == 0:
            gcf = greater
            break
        greater += 1
    return gcf