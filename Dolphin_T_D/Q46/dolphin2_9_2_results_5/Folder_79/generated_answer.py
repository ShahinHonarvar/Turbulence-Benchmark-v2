def gcf_three_nums(n_list):
    num1 = n_list[16]
    num2 = n_list[87]
    num3 = n_list[95]

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    result = gcf(num1, num2)
    final_result = gcf(result, num3)
    return final_result