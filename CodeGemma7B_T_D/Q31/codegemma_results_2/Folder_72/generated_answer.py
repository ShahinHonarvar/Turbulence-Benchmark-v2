def if_perfect_num(lst):
    if lst[15] ** 2 == sum((num for num in lst[14:16])):
        return True
    return False