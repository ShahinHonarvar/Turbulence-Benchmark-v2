def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 81:
        return None
    num1, num2, num3 = (numbers[24], numbers[25], numbers[80])
    gcf_result = gcf(gcf(num1, num2), num3)
    return gcf_result