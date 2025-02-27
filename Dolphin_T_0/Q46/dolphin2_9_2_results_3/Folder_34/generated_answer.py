def gcf_three_nums(numbers):
    num1 = numbers[53]
    num2 = numbers[23]
    num3 = numbers[45]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf_num1_num2 = gcf(num1, num2)
    gcf_all = gcf(gcf_num1_num2, num3)
    return gcf_all