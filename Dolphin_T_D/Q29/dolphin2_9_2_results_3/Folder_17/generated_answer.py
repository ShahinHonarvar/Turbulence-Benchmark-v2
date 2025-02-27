def gcf_two_nums(num_list):

    def gcf(a, b):
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a
    return gcf(num_list[69], num_list[40])