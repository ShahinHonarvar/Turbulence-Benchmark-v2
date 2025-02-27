def find_largest_num(num_list):
    largest = num_list[28]
    for num in num_list[29:33]:
        if num > largest:
            largest = num
    return largest