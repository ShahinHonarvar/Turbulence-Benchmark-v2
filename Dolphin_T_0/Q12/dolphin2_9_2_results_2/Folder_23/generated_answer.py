def find_smallest_num(lst):
    smallest = float('inf')
    for num in lst[59:98]:
        if num < smallest:
            smallest = num
    return smallest