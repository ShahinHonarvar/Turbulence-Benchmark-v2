def gcf_two_nums(arr):

    def gcf(a, b):
        while b > 0:
            a, b = (b, a % b)
        return a
    return gcf(arr[85], arr[51])