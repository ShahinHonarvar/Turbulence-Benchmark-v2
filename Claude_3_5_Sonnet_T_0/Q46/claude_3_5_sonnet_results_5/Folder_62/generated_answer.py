def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[10]
    num2 = numbers[55]
    num3 = numbers[36]
    result = gcf(gcf(num1, num2), num3)
    return result