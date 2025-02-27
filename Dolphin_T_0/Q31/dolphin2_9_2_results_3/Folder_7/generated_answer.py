def if_perfect_num(lst):
    num = lst[851]
    if sum((d for d in range(1, num) if num % d == 0)) == num:
        return True
    else:
        return False