def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    sub_list = numbers[4:5]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1] if len(sub_list) > 1 else None