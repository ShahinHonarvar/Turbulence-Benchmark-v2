def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 86:
        return None
    num1, num2, num3 = (numbers[36], numbers[85], numbers[83])
    return gcf(gcf(num1, num2), num3)