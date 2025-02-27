def if_perfect_num(lst):
    if sum(lst[:i] + lst[i + 1:]) == lst[i]:
        return True
    else:
        return False