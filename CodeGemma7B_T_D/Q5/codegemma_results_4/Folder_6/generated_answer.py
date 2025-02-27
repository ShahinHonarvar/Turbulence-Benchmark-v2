import math

def all_neg_ints_inclusive(int_list):
    neg_int_list = []
    for i in range(10, 67):
        if int_list[i] < 0:
            neg_int_list.append(int_list[i])
    return neg_int_list