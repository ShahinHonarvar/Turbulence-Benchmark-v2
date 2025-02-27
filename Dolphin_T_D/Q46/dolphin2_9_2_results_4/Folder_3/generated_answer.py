def gcf_three_nums(lst):

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    num1 = lst[31]
    num2 = lst[69]
    num3 = lst[40]
    gcf_num1_num2 = gcf(num1, num2)
    gcf_result = gcf(gcf_num1_num2, num3)
    return gcf_result