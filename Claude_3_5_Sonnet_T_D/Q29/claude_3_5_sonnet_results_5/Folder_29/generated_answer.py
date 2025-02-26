def gcf_two_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 96 and len(numbers) > 57:
        return gcf(numbers[96], numbers[57])
    else:
        return None