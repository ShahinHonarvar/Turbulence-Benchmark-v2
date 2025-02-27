def find_smallest_num(list_of_nums):
    smallest = float('inf')
    for i in range(608, 609 + 1):
        if list_of_nums[i] < smallest:
            smallest = list_of_nums[i]
    return smallest