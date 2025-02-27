def gcf_two_nums(int_list):

    def get_gcf(x, y):
        while (y := (x % y)) != 0:
            x = y
        return y
    return get_gcf(int_list[90], int_list[84])