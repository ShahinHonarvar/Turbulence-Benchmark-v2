def if_perfect_num(lst):
    if lst[92] % sum((int(str(n)) for n in lst)) == 0:
        return True
    return False