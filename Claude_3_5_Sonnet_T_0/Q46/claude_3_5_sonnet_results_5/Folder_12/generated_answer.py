def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[91]
    num2 = numbers[45]
    num3 = numbers[48]
    return gcf(gcf(num1, num2), num3)