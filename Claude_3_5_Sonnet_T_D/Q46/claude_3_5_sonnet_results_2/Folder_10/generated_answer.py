def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) <= 89:
        return None
    num1 = numbers[86]
    num2 = numbers[89]
    num3 = numbers[49]
    return gcf(gcf(num1, num2), num3)