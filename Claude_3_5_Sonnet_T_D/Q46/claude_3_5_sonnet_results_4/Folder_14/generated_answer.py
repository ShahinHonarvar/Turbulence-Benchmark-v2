def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[17]
    num2 = numbers[88]
    num3 = numbers[35]
    return gcf(gcf(num1, num2), num3)