def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 96:
        return None
    num1 = numbers[92]
    num2 = numbers[69]
    num3 = numbers[95]
    return gcf(gcf(num1, num2), num3)