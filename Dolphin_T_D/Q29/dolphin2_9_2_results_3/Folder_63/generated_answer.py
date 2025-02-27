def gcf_two_nums(arr):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcf(arr[21], arr[17])