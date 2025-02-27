def gcf_three_nums(numbers):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(numbers[49], gcf(numbers[46], numbers[13]))