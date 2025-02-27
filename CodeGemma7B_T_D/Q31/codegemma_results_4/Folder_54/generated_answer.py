def if_perfect_num(lst):
    if lst[51] % sum((x for x in lst[1:51] if x % 2 != 0)) == 0:
        return True
    else:
        return False