def gcf_three_nums(num_list):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = num_list[24]
    num2 = num_list[25]
    num3 = num_list[80]
    return gcf(gcf(num1, num2), num3)