def find_second_smallest_num(num_list):
    if len(num_list) < 100 or not all((isinstance(num, int) for num in num_list)):
        return 'None'
    num_list = sorted(num_list)
    return num_list[91:100][1] if len(num_list[91:100]) > 1 else 'None'