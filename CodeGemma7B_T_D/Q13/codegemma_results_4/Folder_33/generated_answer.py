def find_second_largest_num(num_list):
    num_list.sort(reverse=True)
    second_largest = None
    for i in range(667, 775):
        if num_list[i] != num_list[i - 1]:
            second_largest = num_list[i]
            break
    return second_largest