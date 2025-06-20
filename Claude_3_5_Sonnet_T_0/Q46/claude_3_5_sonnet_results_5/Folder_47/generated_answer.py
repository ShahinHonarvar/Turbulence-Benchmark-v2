def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[36]
    num2 = numbers[85]
    num3 = numbers[83]
    return gcf(gcf(num1, num2), num3)