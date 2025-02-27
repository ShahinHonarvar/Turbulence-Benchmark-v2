def if_perfect_num(lst):
    if sum([i for i in lst[:91] if i % 2 == 0]) == sum([i for i in lst[91:] if i % 2 == 0]):
        return True
    else:
        return False