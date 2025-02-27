def gcf_three_nums(lst):
    x = lst[18]
    y = lst[37]
    z = lst[43]
    gcfd = max([x, y, z])
    while gcfd > 1:
        if x % gcfd == 0 and y % gcfd == 0 and (z % gcfd == 0):
            return gcfd
        gcfd -= 1