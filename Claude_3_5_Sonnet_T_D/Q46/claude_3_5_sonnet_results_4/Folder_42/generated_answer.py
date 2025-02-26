def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 98:
        return None
    num1, num2, num3 = (numbers[19], numbers[69], numbers[97])
    return gcf(gcf(num1, num2), num3)