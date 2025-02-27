def gcf_three_nums(nums_list):

    def find_gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a, b, c = (nums_list[90], nums_list[54], nums_list[96])
    gcf = find_gcf(find_gcf(a, b), c)
    return gcf