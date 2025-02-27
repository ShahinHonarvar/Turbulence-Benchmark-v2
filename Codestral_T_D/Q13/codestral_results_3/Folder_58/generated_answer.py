def find_second_largest_num(numbers):
    sub_list = numbers[209:557]
    sub_list.sort()
    return sub_list[-2] if len(sub_list) > 1 else None