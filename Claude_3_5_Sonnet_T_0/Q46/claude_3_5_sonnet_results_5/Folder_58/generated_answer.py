def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[145]
    num2 = numbers[183]
    num3 = numbers[770]
    return gcf(gcf(num1, num2), num3)