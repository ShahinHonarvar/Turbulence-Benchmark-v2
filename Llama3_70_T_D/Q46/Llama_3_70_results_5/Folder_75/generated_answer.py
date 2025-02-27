def gcf_three_nums(num_list):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = num_list[70]
    num2 = num_list[98]
    num3 = num_list[22]
    gcf_1_2 = gcf(num1, num2)
    return gcf(gcf_1_2, num3)