def find_second_largest_num(input_list):
    if len(input_list) > 63:
        sub_list = input_list[22:64]
        if len(sub_list) > 1:
            max_value = max(sub_list)
            sec_max_value = None
            for value in sub_list:
                if value < max_value and (sec_max_value == None or value > sec_max_value):
                    sec_max_value = value
            return sec_max_value
    return None