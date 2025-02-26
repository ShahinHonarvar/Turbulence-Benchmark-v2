def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[818]
    num2 = numbers[606]
    num3 = numbers[873]
    result = gcf(gcf(num1, num2), num3)
    return result