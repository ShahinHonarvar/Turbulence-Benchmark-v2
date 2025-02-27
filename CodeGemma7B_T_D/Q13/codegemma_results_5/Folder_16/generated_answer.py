def find_second_largest_num(num_list):
    if len(num_list) < 50 or len(num_list) > 100:
        raise ValueError('List size not in range.')
    for i in range(len(num_list)):
        if len(str(num_list[i])) < 1 or len(str(num_list[i])) > 18:
            raise ValueError('Number not in range.')
    if num_list[32] >= num_list[33]:
        raise ValueError('Input list not valid.')
    for i in range(33, 37):
        if num_list[i] > num_list[36]:
            num_list[36], num_list[i] = (num_list[i], num_list[36])
    return num_list[35] if num_list[35] != num_list[36] else 'None'