def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[99]
    num2 = numbers[63]
    num3 = numbers[74]
    result = gcf(gcf(num1, num2), num3)
    return result