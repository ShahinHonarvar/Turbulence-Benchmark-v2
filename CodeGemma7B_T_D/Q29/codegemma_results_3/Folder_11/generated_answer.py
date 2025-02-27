def gcf_two_nums(int_list):
    num1 = int_list[64]
    num2 = int_list[80]
    common_factor = 1
    while min(num1, num2) >= 1:
        common_factor = max(common_factor, min(num1, num2))
        num1 = num1 % min(num1, num2)
        num2 = num2 % min(num1, num2)
    return common_factor