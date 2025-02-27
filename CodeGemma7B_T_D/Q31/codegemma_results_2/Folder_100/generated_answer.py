def if_perfect_num(array):
    if len(array) >= 100:
        if array[99] in [6, 28, 496, 8128]:
            return True
    return False