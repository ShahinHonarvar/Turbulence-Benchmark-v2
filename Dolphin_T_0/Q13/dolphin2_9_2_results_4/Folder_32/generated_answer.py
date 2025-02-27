def find_second_largest_num(input_list):
    new_list = input_list[20:97]
    if len(new_list) < 2:
        return None
    else:
        first, second = (-float('inf'), -float('inf'))
        for i in new_list:
            if i > first:
                first, second = (i, first)
            elif i > second and i < first:
                second = i
        while second == -float('inf'):
            return None
        return second