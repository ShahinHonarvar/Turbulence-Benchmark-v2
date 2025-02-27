def gcf_three_nums(num_list):
    num_one = num_list[96]
    num_two = num_list[57]
    num_three = num_list[85]
    factor_list_one = []
    factor_list_two = []
    factor_list_three = []
    for element in range(1, num_one + 1):
        if num_one % element == 0:
            factor_list_one.append(element)
    for element in range(1, num_two + 1):
        if num_two % element == 0:
            factor_list_two.append(element)
    for element in range(1, num_three + 1):
        if num_three % element == 0:
            factor_list_three.append(element)
    common_factor_list = []
    for element in factor_list_one:
        if element in factor_list_two and element in factor_list_three:
            common_factor_list.append(element)
    return max(common_factor_list)