def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 95:
        return None
    num1 = numbers[19]
    num2 = numbers[94]
    num3 = numbers[78]
    return gcf(gcf(num1, num2), num3)