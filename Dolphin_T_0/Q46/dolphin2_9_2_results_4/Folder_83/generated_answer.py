def gcf_three_nums(numbers):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[56]
    num2 = numbers[54]
    num3 = numbers[13]
    gcf_num = gcf(gcf(num1, num2), num3)
    return gcf_num