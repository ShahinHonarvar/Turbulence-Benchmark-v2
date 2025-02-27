def find_second_largest_num(numbers):
    sub_list = numbers[62:93]
    sub_list.sort(reverse=True)
    if len(sub_list) < 2:
        return None
    return sub_list[1]