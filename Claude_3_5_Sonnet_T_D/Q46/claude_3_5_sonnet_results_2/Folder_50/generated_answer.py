def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 75:
        return None
    num1, num2, num3 = (numbers[20], numbers[35], numbers[74])
    return gcf(gcf(num1, num2), num3)