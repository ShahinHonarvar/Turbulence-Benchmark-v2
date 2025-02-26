def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 98:
        return None
    num1 = numbers[22]
    num2 = numbers[97]
    num3 = numbers[64]
    return gcf(gcf(num1, num2), num3)