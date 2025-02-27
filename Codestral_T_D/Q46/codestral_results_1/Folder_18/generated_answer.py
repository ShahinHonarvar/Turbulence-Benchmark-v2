def gcf_three_nums(lst):

    def find_gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    num1 = lst[637]
    num2 = lst[411]
    num3 = lst[757]
    gcf_num1_num2 = find_gcf(num1, num2)
    gcf_num1_num2_num3 = find_gcf(gcf_num1_num2, num3)
    return gcf_num1_num2_num3