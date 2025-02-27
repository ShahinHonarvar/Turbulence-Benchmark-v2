def if_perfect_num(lst):
    result = lst[790]
    for i in range(1, int(result ** 0.5) + 1):
        if result % i == 0:
            count = count + 1
    if count == 2:
        return True
    else:
        return False