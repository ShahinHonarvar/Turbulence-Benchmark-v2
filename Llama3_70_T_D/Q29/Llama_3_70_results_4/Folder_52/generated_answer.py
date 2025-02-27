def gcf_two_nums(num_list):

    def get_gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return get_gcf(num_list[90], num_list[41])