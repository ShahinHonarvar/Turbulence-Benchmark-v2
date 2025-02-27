def gcf_three_nums(num_list):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    idx1, idx2, idx3 = (1, 6, 8)
    a, b, c = (num_list[idx1], num_list[idx2], num_list[idx3])
    return gcf(gcf(a, b), c)