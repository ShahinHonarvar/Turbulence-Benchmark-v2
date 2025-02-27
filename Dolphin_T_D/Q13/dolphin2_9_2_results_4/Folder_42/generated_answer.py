def find_second_largest_num(input_list):
    if len(input_list) == 0 or len(input_list) < 80:
        return 'None'
    else:
        sub_list = input_list[29:80]
        if len(sub_list) < 2:
            return 'None'
        else:
            first_largest = max(sub_list)
            sub_list.remove(first_largest)
            return max(sub_list)