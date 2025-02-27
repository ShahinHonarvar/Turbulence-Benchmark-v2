def if_perfect_num(lst):
    if len(lst) <= 95:
        return False
    n = lst[95]
    return sum((i for i in range(1, n) if n % i == 0)) == n