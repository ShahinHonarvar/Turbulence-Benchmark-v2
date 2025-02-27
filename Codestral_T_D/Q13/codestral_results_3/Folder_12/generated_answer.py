def find_second_largest_num(numbers):
    sub_list = sorted(numbers[14:65], reverse=True)
    if len(sub_list) < 2:
        return None
    return sub_list[1]