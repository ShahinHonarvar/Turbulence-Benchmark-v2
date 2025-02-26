def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 89:
        return None
    num1 = numbers[17]
    num2 = numbers[35]
    num3 = numbers[88]
    return gcf(gcf(num1, num2), num3)