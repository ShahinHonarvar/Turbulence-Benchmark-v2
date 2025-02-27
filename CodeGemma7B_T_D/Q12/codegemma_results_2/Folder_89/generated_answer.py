def find_smallest_num(list):
    smallest = float('inf')
    for i in range(22, 51):
        if list[i] < smallest:
            smallest = list[i]
    return smallest