def gcf_three_nums(nums_list):
    num1 = nums_list[40]
    num2 = nums_list[15]
    num3 = nums_list[99]

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    result = gcf(num1, num2)
    final_result = gcf(result, num3)
    return final_result