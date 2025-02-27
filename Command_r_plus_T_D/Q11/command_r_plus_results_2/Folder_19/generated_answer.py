def find_largest_num(num_list):
    largest = num_list[3]
    for num in num_list[4:6]:
        if num > largest:
            largest = num
    return largest