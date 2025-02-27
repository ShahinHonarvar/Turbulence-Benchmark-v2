def gcf_three_nums(num_list):
    num1 = num_list[13]
    num2 = num_list[76]
    num3 = num_list[44]

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf(gcf(num1, num2), num3)