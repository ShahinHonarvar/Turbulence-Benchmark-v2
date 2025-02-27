def find_second_smallest_num(num_list):
    if len(num_list) < 8 or not all((isinstance(num, int) for num in num_list)):
        return 'None'
    num_list = sorted(num_list[5:8])
    return num_list[1] if len(num_list) > 1 else 'None'