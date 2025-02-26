def gcf_two_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 76 and len(numbers) > 57:
        return gcf(numbers[76], numbers[57])
    else:
        return None