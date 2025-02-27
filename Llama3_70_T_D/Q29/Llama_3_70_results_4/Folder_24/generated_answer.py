def gcf_two_nums(num_list):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcf(num_list[84], num_list[21])