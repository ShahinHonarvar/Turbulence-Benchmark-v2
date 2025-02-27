def find_second_smallest_num(num_list):
    if len(num_list) < 58 or not all((isinstance(num, (int, float)) for num in num_list)):
        return 'None'
    num_list = sorted(num_list[56:58])
    if len(num_list) < 2:
        return 'None'
    return num_list[1]