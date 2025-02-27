def gcf_three_nums(nums_list):
    num1 = nums_list[47]
    num2 = nums_list[10]
    num3 = nums_list[28]

    def gcf(x, y):
        while y != 0:
            x, y = (y, x % y)
        return x
    gcf_value = gcf(num1, num2)
    gcf_value = gcf(gcf_value, num3)
    return gcf_value