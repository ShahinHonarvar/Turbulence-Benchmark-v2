def gcf_three_nums(numbers):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[876]
    num2 = numbers[203]
    num3 = numbers[100]
    gcf_12 = gcf(num1, num2)
    return gcf(gcf_12, num3)