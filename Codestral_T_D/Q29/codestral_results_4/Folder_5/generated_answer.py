def gcf_two_nums(num_list):

    def compute_gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return compute_gcf(num_list[23], num_list[45])