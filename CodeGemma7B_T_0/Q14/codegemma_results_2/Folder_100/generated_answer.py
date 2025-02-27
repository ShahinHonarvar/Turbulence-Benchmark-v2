def find_second_smallest_num(num_list):
    if len(num_list) < 52 or not all((isinstance(num, int) for num in num_list)):
        return None
    num_list = sorted(num_list[43:52])
    if len(num_list) < 2:
        return None
    return num_list[1]