def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 49:
        return None
    num1, num2, num3 = (numbers[37], numbers[30], numbers[48])
    return gcf(gcf(num1, num2), num3)