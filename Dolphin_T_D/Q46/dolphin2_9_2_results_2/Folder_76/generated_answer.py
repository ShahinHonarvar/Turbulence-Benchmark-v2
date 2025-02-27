def gcf_three_nums(nums_list):
    num1 = nums_list[876]
    num2 = nums_list[203]
    num3 = nums_list[100]

    def gcf(num1, num2):
        while num2 != 0:
            num1, num2 = (num2, num1 % num2)
        return num1
    result = gcf(num1, num2)
    result = gcf(result, num3)
    return result