def find_smallest_num(num_list):
    smallest = float('inf')
    for num in num_list[10:67]:
        if num < smallest:
            smallest = num
    return smallest