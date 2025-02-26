def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 565:
        return None
    num1 = numbers[252]
    num2 = numbers[149]
    num3 = numbers[564]
    return gcf(gcf(num1, num2), num3)