def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_three(a, b, c):
        return gcf(gcf(a, b), c)
    return gcf_three(numbers[4], numbers[0], numbers[8])