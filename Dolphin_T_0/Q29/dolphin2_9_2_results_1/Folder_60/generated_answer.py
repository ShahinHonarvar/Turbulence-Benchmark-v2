def gcf_two_nums(num_list):

    def gcf(a, b):
        if a == 0:
            return b
        return gcf(b % a, a)
    return gcf(num_list[28], num_list[53])