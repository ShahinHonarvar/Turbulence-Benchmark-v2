def gcf_three_nums(num_list):
    num1 = num_list[31]
    num2 = num_list[69]
    num3 = num_list[40]

    def gcf(a, b):
        if b == 0:
            return a
        else:
            return gcf(b, a % b)
    return gcf(gcf(num1, num2), num3)