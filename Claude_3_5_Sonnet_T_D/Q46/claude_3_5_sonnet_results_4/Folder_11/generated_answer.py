def gcf_three_nums(num_list):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = num_list[37]
    num2 = num_list[30]
    num3 = num_list[48]
    return gcf(gcf(num1, num2), num3)