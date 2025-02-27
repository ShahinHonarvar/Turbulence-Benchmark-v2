def gcf_two_nums(num_list):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(num_list[78], num_list[16])