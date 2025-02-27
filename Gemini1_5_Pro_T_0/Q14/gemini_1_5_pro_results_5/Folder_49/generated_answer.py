def find_second_smallest_num(numbers):
    sub_list = numbers[80:201]
    if len(sub_list) < 2:
        return None
    else:
        sorted_list = sorted(sub_list)
        return sorted_list[1]