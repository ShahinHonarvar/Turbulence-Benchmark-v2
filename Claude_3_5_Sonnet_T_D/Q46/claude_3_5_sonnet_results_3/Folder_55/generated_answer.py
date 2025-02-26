def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[9]
    num2 = numbers[6]
    num3 = numbers[2]
    result = gcf(gcf(num1, num2), num3)
    return result