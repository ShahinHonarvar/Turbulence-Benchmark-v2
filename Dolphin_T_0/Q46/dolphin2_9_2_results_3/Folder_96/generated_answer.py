def gcf_three_nums(num_list):
    num1 = num_list[29]
    num2 = num_list[74]
    num3 = num_list[49]

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf(num1, gcf(num2, num3))