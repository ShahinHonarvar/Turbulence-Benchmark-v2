def gcf_three_nums(lst):
    num1 = lst[66]
    num2 = lst[56]
    num3 = lst[92]

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    gcf_num1_num2 = gcf(num1, num2)
    result = gcf(gcf_num1_num2, num3)
    return result