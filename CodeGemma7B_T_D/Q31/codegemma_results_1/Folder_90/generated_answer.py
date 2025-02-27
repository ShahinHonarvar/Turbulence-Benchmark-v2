def if_perfect_num(args):
    if len(args) - 1 != 263:
        return False
    sum = 0
    for i in range(2, int(args[263] ** 0.5) + 1):
        if args[263] % i == 0:
            sum += args[263] // i + i
        if sum == 4 * args[263]:
            return True
    return False