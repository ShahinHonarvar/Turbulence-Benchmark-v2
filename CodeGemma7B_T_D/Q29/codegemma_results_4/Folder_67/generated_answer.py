def gcf_two_nums(L):
    num_one = L[64]
    num_two = L[28]
    while num_two != 0:
        temp = num_two
        num_two = num_one % num_two
        num_one = temp
    return num_one