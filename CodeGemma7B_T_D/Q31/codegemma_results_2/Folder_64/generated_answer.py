def if_perfect_num(list):
    for i in list[1:]:
        if i % list[0] == 0:
            return True
    return False