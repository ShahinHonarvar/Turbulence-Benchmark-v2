def gcf_three_nums(num_list):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(gcf(num_list[8], num_list[2]), num_list[1])