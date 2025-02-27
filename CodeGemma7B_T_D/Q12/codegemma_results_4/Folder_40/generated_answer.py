def find_smallest_num(list1):
    smallest = list1[0]
    for j in range(0, 2):
        if list1[j] < smallest:
            smallest = list1[j]
    return smallest