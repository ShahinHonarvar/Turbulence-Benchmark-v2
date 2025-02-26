def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1, num2, num3 = (numbers[1], numbers[6], numbers[8])
    return gcf(gcf(num1, num2), num3)