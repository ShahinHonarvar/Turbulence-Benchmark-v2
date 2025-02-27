def find_largest_num(num_list):
    largest = num_list[10]
    for num in num_list[10:67]:
        if num > largest:
            largest = num
    return largest