def gcf_three_nums(num_list):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf_558_110 = gcf(num_list[558], num_list[110])
    return gcf(gcf_558_110, num_list[628])