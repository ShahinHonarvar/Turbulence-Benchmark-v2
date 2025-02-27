def find_largest_num(numbs):
    largest_num = numbs[0]
    for num in numbs:
        if num > largest_num:
            largest_num = num
    return largest_num