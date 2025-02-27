def find_largest_num(num_list):
    largest = num_list[17]
    for i in num_list[18:79]:
        if i > largest:
            largest = i
    return largest