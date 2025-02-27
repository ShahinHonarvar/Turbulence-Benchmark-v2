def gcf_three_nums(num_list):
    num1 = num_list[16]
    num2 = num_list[87]
    num3 = num_list[95]

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    result = gcf(num1, num2)
    result = gcf(result, num3)
    return result