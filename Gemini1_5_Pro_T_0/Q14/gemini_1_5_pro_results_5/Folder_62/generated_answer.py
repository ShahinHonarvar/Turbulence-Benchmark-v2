def find_second_smallest_num(numbers):
    if len(numbers) < 67:
        return None
    sub_list = numbers[10:67]
    if len(set(sub_list)) < 2:
        return None
    sorted_list = sorted(sub_list)
    return sorted_list[1]