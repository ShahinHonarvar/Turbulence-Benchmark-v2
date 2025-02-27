def gcf_three_nums(numbers):
    nums = [numbers[44], numbers[91], numbers[42]]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return reduce(gcf, nums)