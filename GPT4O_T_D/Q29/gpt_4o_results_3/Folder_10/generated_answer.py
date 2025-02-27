def gcf_two_nums(numbers):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    if len(numbers) < 100:
        return None
    return gcf(numbers[15], numbers[99])