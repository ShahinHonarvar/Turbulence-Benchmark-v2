def find_smallest_num(list1):
    smallest = list1[0]
    for i in range(0, 2):
        if list1[i] < smallest:
            smallest = list1[i]
    return smallest