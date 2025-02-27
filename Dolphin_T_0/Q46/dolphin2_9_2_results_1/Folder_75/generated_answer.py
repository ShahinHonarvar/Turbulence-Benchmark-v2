def gcf_three_nums(num_list):
    num1 = num_list[70]
    num2 = num_list[98]
    num3 = num_list[22]

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    return gcf(gcf(num1, num2), num3)