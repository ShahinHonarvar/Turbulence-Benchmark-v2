def gcf_three_nums(numbers):
    a = numbers[90]
    b = numbers[54]
    c = numbers[96]

    def gcf(a, b):
        if b == 0:
            return a
        else:
            return gcf(b, a % b)
    return gcf(gcf(a, b), c)