def gcf_three_nums(numbers):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(gcf(numbers[427], numbers[761]), numbers[148])