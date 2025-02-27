def gcf_three_nums(num_list):
    num1 = num_list[654]
    num2 = num_list[312]
    num3 = num_list[441]

    def gcf(a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        if a == b:
            return a
        if a > b:
            return gcf(a - b, b)
        return gcf(a, b - a)
    return gcf(gcf(num1, num2), num3)