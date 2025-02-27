def find_largest_num(num_list):
    largest = num_list[5]
    for num in num_list[6:8]:
        if num > largest:
            largest = num
    return largest