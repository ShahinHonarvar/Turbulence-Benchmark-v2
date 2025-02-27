def gcf_three_nums(numbers):
    num1 = numbers[16]
    num2 = numbers[87]
    num3 = numbers[95]

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcf(gcf(num1, num2), num3)