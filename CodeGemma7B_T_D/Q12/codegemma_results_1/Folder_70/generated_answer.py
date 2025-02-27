def find_smallest_num(num_list):
    smallest = num_list[30]
    for num in num_list[31:49]:
        if num < smallest:
            smallest = num
    return smallest