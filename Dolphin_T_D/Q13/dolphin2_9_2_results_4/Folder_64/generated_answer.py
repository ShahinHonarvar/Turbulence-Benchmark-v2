def find_second_largest_num(num_list):
    if len(num_list) == 0:
        return None
    elif len(num_list) == 1:
        return None
    else:
        first_max = second_max = float('-inf')
        for i in num_list[0:5]:
            if i > first_max:
                first_max, second_max = (i, first_max)
            elif first_max > i > second_max:
                second_max = i
        if second_max == float('-inf'):
            return None
        else:
            return second_max