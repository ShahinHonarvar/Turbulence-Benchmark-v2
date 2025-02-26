def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[990]
    num2 = numbers[671]
    num3 = numbers[711]
    result = gcf(gcf(num1, num2), num3)
    return result