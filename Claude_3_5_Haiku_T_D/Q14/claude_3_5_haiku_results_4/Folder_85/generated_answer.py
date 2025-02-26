def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 7:
        return None
    sub_list = numbers[0:7]
    sorted_sub_list = sorted(set(sub_list))
    return sorted_sub_list[1] if len(sorted_sub_list) > 1 else None