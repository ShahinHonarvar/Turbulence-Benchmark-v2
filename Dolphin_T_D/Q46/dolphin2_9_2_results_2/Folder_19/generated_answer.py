def gcf_three_nums(num_list):
    num1 = num_list[40]
    num2 = num_list[15]
    num3 = num_list[99]

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf(gcf(num1, num2), num3)