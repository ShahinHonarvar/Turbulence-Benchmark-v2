def find_smallest_num(list):
    smallest_num = float('inf')
    for i in range(75, 89):
        if list[i] < smallest_num:
            smallest_num = list[i]
    return smallest_num