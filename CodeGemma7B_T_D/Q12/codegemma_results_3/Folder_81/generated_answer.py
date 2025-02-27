from sys import maxsize

def find_smallest_num(num_list):
    smallest = maxsize
    for num in num_list[10:101]:
        if num < smallest:
            smallest = num
    return smallest