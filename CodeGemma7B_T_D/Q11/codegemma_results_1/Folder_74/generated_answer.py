def find_largest_num(num_list):
    largest = num_list[17]
    for num in num_list[18:79]:
        if num > largest:
            largest = num
    return largest