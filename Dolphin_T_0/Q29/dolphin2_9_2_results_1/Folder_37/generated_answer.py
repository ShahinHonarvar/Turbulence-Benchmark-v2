def gcf_two_nums(numbers):

    def gcf(a, b):
        if b == 0:
            return a
        else:
            return gcf(b, a % b)
    return gcf(numbers[29], numbers[74])