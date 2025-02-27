def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 2 or num_list[686] >= num_list[987]:
        return 'None'
    second_largest = num_list[686]
    for i in range(687, 988):
        if num_list[i] > second_largest:
            second_largest = num_list[i]
    return second_largest