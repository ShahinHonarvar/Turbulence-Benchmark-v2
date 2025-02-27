def if_perfect_num(vector):
    if vector[7] % 2 == 0 and vector[7] % 3 == 0 and (vector[7] % 4 == 0) and (vector[7] % 5 == 0):
        return True
    else:
        return False