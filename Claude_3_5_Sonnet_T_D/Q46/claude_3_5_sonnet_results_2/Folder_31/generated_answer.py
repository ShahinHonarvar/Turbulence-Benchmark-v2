def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[90]
    num2 = numbers[54]
    num3 = numbers[96]
    result = gcf(gcf(num1, num2), num3)
    return result