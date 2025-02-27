def gcf_two_nums(num_list):

    def gcf(a, b):
        if b == 0:
            return a
        else:
            return gcf(b, a % b)
    return gcf(num_list[29], num_list[74])