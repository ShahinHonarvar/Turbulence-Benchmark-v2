def gcf_three_nums(num_list):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = num_list[912]
    num2 = num_list[170]
    num3 = num_list[500]
    return gcf(gcf(num1, num2), num3)