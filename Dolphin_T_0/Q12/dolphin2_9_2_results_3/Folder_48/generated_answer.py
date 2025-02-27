def find_smallest_num(numbers_list):
    smallest = None
    for i in range(209, 557):
        if smallest is None or numbers_list[i] < smallest:
            smallest = numbers_list[i]
    return smallest