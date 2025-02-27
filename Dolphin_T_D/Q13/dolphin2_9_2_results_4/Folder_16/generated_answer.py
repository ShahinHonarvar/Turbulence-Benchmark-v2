def find_second_largest_num(num_list):
    sub_list = num_list[33:37]
    if len(set(sub_list)) < 2:
        return None
    else:
        first_largest = max(sub_list)
        second_largest = None
        for num in sub_list:
            if num != first_largest:
                if second_largest is None or num > second_largest:
                    second_largest = num
        return second_largest