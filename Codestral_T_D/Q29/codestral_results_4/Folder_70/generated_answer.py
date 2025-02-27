def gcf_two_nums(num_list):

    def find_gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return find_gcf(num_list[300], num_list[616])