def gcf_two_nums(lst):

    def gcf(a, b):
        r = a % b
        while r != 0:
            a = b
            b = r
            r = a % b
        return b
    return gcf(lst[129], lst[582])