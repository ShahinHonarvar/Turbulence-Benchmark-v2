def gcf_two_nums(numbers):

    def compute_gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return compute_gcf(numbers[13], numbers[66])