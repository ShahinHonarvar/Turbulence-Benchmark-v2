def find_second_largest_num(numbers):
    if len(numbers) < 89:
        return None
    sub_list = numbers[22:89]
    sub_list.sort(reverse=True)
    if len(sub_list) < 2:
        return None
    return sub_list[1]