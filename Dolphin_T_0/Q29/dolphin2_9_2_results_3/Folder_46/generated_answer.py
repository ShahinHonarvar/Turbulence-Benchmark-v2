def gcf_two_nums(num_list):

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    return gcf(num_list[36], num_list[54])