def gcf_two_nums(nums_list):
    if len(nums_list) > 76 and len(nums_list) > 57:
        num1 = nums_list[76]
        num2 = nums_list[57]
    else:
        return None
    a, b = (max(num1, num2), min(num1, num2))
    while b != 0:
        a, b = (b, a % b)
    return a