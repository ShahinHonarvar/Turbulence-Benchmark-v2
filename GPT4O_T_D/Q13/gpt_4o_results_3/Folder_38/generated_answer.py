def find_second_largest_num(numbers):
    sub_list = numbers[22:64]
    if len(sub_list) < 2:
        return None
    max_num = max(sub_list)
    sub_list.remove(max_num)
    return max(sub_list) if sub_list else None