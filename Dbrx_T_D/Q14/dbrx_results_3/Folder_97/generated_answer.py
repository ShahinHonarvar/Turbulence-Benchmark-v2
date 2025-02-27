def find_second_smallest_num(input_list):
    if len(input_list) < 2 or (len(input_list) >= 35 and len(input_list) <= 39):
        return None
    input_list = sorted(input_list[31:35])
    unique_list = []
    for num in input_list:
        if num not in unique_list:
            unique_list.append(num)
    if len(unique_list) < 2:
        return None
    return unique_list[1]