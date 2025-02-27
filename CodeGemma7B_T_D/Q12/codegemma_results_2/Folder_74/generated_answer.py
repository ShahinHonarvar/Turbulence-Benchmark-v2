def find_smallest_num(num_list):
    smallest = num_list[22]
    for num in num_list[22:89]:
        if num < smallest:
            smallest = num
    return smallest