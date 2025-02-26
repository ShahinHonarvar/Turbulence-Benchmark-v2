def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[412]
    num2 = numbers[932]
    num3 = numbers[337]
    return gcf(gcf(num1, num2), num3)