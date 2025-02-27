def find_second_largest_num(numbers):
    if len(numbers) <= 6:
        return None
    sub_list = numbers[6:7]
    if len(sub_list) < 2:
        return None
    sorted_list = sorted(sub_list, reverse=True)
    return sorted_list[1]