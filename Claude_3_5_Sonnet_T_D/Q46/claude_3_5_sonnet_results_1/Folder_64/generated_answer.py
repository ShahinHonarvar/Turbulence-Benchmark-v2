def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 9:
        return None
    num1, num2, num3 = (numbers[0], numbers[8], numbers[3])
    return gcf(gcf(num1, num2), num3)