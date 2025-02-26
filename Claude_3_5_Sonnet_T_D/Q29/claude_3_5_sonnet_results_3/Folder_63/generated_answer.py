def gcf_two_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 21 and len(numbers) > 17:
        return gcf(numbers[21], numbers[17])
    else:
        return None