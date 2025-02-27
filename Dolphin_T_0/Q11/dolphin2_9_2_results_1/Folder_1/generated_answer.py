def find_largest_num(lst):
    largest = None
    for num in lst[31:73]:
        if largest is None or num > largest:
            largest = num
    return largest