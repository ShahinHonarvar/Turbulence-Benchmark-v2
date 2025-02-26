def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 91:
        return None
    num1 = numbers[90]
    num2 = numbers[84]
    num3 = numbers[47]
    return gcf(gcf(num1, num2), num3)