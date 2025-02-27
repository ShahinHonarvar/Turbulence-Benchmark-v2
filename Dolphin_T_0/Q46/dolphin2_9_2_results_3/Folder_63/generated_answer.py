def gcf_three_nums(lst):
    numbers = [lst[38], lst[52], lst[69]]

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x

    def gcf_three(x, y, z):
        gcf_xy = gcf(x, y)
        gcf_yz = gcf(y, z)
        return gcf(gcf_xy, gcf_yz)
    return gcf_three(*numbers)