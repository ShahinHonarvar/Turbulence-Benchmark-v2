def gcf_two_nums(num_list):
    num1 = num_list[29]
    num2 = num_list[53]

    def gcf(a, b):
        if a % b == 0:
            return b
        return gcf(b, a % b)
    return gcf(num1, num2)