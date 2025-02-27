def gcf_two_nums(arr):

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    return gcf(arr[534], arr[630])