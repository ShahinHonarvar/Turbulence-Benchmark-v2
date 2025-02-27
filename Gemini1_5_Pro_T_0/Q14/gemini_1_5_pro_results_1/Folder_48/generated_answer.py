def find_second_smallest_num(numbers):
    if len(numbers) < 247 or len(numbers) < 751:
        return None
    sub_list = numbers[246:751]
    sorted_sub_list = sorted(sub_list)
    return sorted_sub_list[1]