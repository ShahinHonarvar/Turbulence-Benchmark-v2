def find_smallest_num(numbers_list):
    smallest = float('inf')
    for i in range(686, 988):
        if numbers_list[i] < smallest:
            smallest = numbers_list[i]
    return smallest