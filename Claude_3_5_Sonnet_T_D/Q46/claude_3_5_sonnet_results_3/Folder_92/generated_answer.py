def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[7]
    num2 = numbers[9]
    num3 = numbers[0]
    result = gcf(gcf(num1, num2), num3)
    return result