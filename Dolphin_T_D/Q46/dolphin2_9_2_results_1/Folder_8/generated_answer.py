def gcf_three_nums(arr):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    modulo = arr[99]
    modulo = gcf(modulo, arr[28])
    modulo = gcf(modulo, arr[53])
    return modulo