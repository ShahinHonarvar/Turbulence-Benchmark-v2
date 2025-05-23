def find_second_smallest_num(num_list):
    if len(num_list) < 10 or not all((isinstance(num, (int, float)) for num in num_list)):
        return 'None'
    num_list = num_list[8:10]
    num_list.sort()
    if len(num_list) < 2:
        return 'None'
    return num_list[1]