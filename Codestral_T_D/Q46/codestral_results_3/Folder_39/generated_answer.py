def gcf_three_nums(numbers):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(gcf(numbers[85], numbers[36]), numbers[54])