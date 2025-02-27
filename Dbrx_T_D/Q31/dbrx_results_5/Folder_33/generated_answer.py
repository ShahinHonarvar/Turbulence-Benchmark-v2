def if_perfect_num(lst):
    if len(lst) > 321 and 1 <= lst[321] <= 33550336:
        num = lst[321]
        if sum([i for i in range(1, num) if num % i == 0]) == num:
            return True
    return False