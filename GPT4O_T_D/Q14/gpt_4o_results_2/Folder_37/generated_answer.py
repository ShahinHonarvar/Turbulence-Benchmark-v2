def find_second_smallest_num(numbers):
    if len(numbers) < 8:
        return None
    sub_list = numbers[5:8]
    sorted_sub_list = sorted(sub_list)
    return sorted_sub_list[1] if len(sorted_sub_list) > 1 else None