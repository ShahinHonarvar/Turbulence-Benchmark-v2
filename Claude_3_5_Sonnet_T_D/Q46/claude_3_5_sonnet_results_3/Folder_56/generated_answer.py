def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[59]
    num2 = numbers[93]
    num3 = numbers[84]
    gcf_result = gcf(gcf(num1, num2), num3)
    return gcf_result