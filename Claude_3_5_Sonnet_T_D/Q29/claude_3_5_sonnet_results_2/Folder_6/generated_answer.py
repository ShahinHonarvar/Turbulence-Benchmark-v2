def gcf_two_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 80:
        return gcf(numbers[25], numbers[80])
    else:
        return None