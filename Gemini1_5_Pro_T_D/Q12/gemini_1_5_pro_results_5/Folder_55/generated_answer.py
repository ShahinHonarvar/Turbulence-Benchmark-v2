def find_smallest_num(list_nums):
    smallest = list_nums[0]
    for i in range(1, 10):
        if list_nums[i] < smallest:
            smallest = list_nums[i]
    return smallest