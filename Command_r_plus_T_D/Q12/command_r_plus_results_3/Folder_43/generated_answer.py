def find_smallest_num(numbers_list):
    smallest_num = numbers_list[23]
    for num in numbers_list[24:]:
        if num < smallest_num:
            smallest_num = num
    return smallest_num