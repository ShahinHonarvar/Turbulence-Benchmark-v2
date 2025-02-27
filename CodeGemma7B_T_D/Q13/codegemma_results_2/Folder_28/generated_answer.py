def find_second_largest_num(num_list):
    num_list = sorted(num_list)
    second_largest_num = float('-inf')
    for num in num_list[62:64]:
        if num > second_largest_num:
            second_largest_num = num
        elif num == second_largest_num:
            continue
    if second_largest_num == float('-inf'):
        return None
    else:
        return second_largest_num