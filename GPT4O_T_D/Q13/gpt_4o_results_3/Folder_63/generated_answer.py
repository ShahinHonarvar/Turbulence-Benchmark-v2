def find_second_largest_num(numbers):
    if len(numbers) < 89:
        return None
    sub_list = numbers[22:89]
    if len(sub_list) < 2:
        return None
    sub_list = list(set(sub_list))
    sub_list.sort(reverse=True)
    if len(sub_list) < 2:
        return None
    return sub_list[1]