def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 46:
        return None
    num1 = numbers[24]
    num2 = numbers[38]
    num3 = numbers[45]
    return gcf(gcf(num1, num2), num3)