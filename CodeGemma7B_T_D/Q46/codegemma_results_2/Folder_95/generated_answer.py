def gcf_three_nums(list_of_nums):
    num1 = list_of_nums[87]
    num2 = list_of_nums[20]
    num3 = list_of_nums[36]
    common_factor = gcf(num1, gcf(num2, num3))
    return common_factor

def gcf(num1, num2):
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1