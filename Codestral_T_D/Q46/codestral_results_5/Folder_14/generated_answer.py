def gcf_three_nums(num_list):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcf(gcf(num_list[17], num_list[88]), num_list[35])