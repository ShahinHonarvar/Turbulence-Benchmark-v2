def gcf_three_nums(numbers):
    index1, index2, index3 = (25, 76, 57)
    num1, num2, num3 = (numbers[index1], numbers[index2], numbers[index3])

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf(gcf(num1, num2), num3)