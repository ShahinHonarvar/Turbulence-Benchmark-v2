def gcf_two_nums(nums_list):
    num1 = nums_list[96]
    num2 = nums_list[57]
    a, b = (max(num1, num2), min(num1, num2))
    while b != 0:
        a, b = (b, a % b)
    return a