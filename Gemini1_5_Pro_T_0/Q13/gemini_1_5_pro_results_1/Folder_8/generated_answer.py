def find_second_largest_num(numbers):
    if len(numbers) < 2 or 23 >= len(numbers) or 23 < 0:
        return None
    sub_list = numbers[23:24]
    if len(sub_list) < 2:
        return None
    largest = max(sub_list)
    sub_list.remove(largest)
    if len(sub_list) == 0:
        return None
    return max(sub_list)