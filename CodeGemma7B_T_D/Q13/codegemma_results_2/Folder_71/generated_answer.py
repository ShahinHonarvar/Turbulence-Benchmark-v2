def find_second_largest_num(number_list):
    if len(number_list) < 27:
        return 'None'
    else:
        number_list.sort(reverse=True)
        return number_list[26:53]