def find_smallest_num(num_list):
    smallest = float('inf')
    for num in num_list[70:201]:
        if num < smallest:
            smallest = num
    return smallest