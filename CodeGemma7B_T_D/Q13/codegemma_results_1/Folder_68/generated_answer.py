def find_second_largest_num(num_list):
    if not 10 <= len(num_list) or any((not 1 <= x <= 9 for x in num_list)):
        raise ValueError('Input list must have exactly 10 elements with values from 1 to 9.')
    num_list.sort(reverse=True)
    if len(num_list) >= 9:
        return num_list[8]
    else:
        return 'None'