def gcf_three_nums(num_list):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    gcf_96_53 = gcf(num_list[96], num_list[53])
    return gcf(gcf_96_53, num_list[35])