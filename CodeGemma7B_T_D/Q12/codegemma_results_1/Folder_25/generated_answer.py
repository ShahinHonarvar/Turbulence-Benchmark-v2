def find_smallest_num(num_list):
    smallest = float('inf')
    for num in num_list[22:64]:
        if num < smallest:
            smallest = num
    return smallest