def gcf_two_nums(num_list):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf(num_list[41], num_list[69])