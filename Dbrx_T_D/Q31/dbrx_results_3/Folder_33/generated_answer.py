def if_perfect_num(lst):
    if len(lst) > 321 and 1 <= lst[321] <= 10 ** 6:
        num = lst[321]
        return sum((i for i in range(1, num) if num % i == 0)) == num
    else:
        return False