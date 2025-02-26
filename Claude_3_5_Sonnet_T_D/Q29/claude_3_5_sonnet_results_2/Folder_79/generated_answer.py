def gcf_two_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 85 and len(numbers) > 51:
        return gcf(numbers[85], numbers[51])
    else:
        return None