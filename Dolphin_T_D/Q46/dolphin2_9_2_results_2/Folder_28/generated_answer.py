def gcf_three_nums(numbers):

    def gcf(a, b):
        if b == 0:
            return a
        else:
            return gcf(b, a % b)
    num1 = numbers[99]
    num2 = numbers[63]
    num3 = numbers[74]
    gcf_1_2 = gcf(num1, num2)
    gcf_of_all = gcf(gcf_1_2, num3)
    return gcf_of_all