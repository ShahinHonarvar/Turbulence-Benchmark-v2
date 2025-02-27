def find_smallest_num(numbers_list):
    smallest = numbers_list[23]
    for num in numbers_list[24:]:
        if num < smallest:
            smallest = num
    return smallest