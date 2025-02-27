def gcf_two_nums(mylist):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcf(mylist[15], mylist[99])