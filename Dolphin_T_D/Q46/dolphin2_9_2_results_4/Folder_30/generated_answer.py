def gcf_three_nums(numbers):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcf(numbers[76], gcf(numbers[35], numbers[74]))