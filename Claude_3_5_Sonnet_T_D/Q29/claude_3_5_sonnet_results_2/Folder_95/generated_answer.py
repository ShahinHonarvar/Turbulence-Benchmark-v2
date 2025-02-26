def gcf_two_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 99:
        return gcf(numbers[43], numbers[99])
    else:
        return None