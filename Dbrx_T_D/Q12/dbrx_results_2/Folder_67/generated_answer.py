def find_smallest_num(numbers_list):
    if len(numbers_list) < 62:
        return 'List must have at least 62 elements'
    else:
        sub_list = numbers_list[61:100]
        return min(sub_list)