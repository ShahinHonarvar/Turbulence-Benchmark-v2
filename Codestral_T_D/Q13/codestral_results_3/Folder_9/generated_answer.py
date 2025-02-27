def find_second_largest_num(numbers):
    if 200 >= len(numbers):
        return None
    else:
        sub_list = numbers[200:201]
        sub_list.sort()
        return sub_list[-2] if len(sub_list) > 1 else None