def gcf_three_nums(lst):
    num1 = lst[1]
    num2 = lst[6]
    num3 = lst[8]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf_num = gcf(num1, num2)
    gcf_result = gcf(gcf_num, num3)
    return gcf_result