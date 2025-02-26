def gcf_two_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 88 and len(numbers) > 35:
        return gcf(numbers[88], numbers[35])
    else:
        return None