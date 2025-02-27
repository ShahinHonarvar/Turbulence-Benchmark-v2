def find_largest_num(num_list):
    largest = num_list[6]
    for num in num_list[7:9]:
        if num > largest:
            largest = num
    return largest