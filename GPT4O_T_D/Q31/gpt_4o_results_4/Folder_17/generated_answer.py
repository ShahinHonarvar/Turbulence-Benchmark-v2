def if_perfect_num(lst):
    if lst and len(lst) > 632:
        num = lst[632]
        return num > 1 and sum((i for i in range(1, num) if num % i == 0)) == num
    return False