def find_largest_num(list):
    current_largest = list[0]
    for num in list[1:]:
        if num > current_largest:
            current_largest = num
    return current_largest