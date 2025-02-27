def find_second_smallest_num(numbers):
    if len(numbers) < 94:
        return None
    sub_list = numbers[29:94]
    if len(set(sub_list)) < 2:
        return None
    sorted_list = sorted(sub_list)
    return sorted_list[1]