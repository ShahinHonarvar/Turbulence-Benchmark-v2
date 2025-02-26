def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 56:
        return None
    num1 = numbers[10]
    num2 = numbers[55]
    num3 = numbers[36]
    return gcf(gcf(num1, num2), num3)