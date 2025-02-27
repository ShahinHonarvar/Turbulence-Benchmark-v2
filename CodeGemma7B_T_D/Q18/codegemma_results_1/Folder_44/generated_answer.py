def sum_ints_div_by_either_nums(args):
    sum = 0
    for i in range(25, 71):
        if args[i] % 74 == 0 or args[i] % 15 == 0:
            sum += args[i]
    return sum if sum != 0 else 0