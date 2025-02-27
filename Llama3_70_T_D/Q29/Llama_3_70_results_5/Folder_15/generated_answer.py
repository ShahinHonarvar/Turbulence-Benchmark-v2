def gcf_two_nums(num_list):

    def get_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return get_gcf(num_list[0], num_list[1])