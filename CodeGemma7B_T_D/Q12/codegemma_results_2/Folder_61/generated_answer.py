def find_smallest_num(num_list):
    smallest = num_list[0]
    for num in num_list[0:7]:
        if num < smallest:
            smallest = num
    return smallest