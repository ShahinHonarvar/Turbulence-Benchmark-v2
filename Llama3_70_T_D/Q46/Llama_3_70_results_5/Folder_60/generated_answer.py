def gcf_three_nums(num_list):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(num_list[96], gcf(num_list[53], num_list[35]))