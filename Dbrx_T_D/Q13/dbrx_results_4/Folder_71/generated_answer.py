def find_second_largest_num(numbers):
    if len(numbers) < 27:
        return None
    sub_list = numbers[26:53]
    sub_set = set(sub_list)
    if len(sub_set) < 2:
        return None
    sub_list.sort(reverse=True)
    return sub_list[1] if sub_list[1] != sub_list[0] else None