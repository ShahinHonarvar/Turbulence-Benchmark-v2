def gcf_two_nums(int_list):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcf(int_list[19], int_list[94])