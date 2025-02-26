def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 71:
        return None
    num1 = numbers[13]
    num2 = numbers[32]
    num3 = numbers[70]
    return gcf(gcf(num1, num2), num3)