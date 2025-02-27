def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 7:
        return None
    sub_list = numbers[:7]
    sorted_sub_list = sorted(sub_list, reverse=True)
    return sorted_sub_list[1] if len(sorted_sub_list) >= 2 else None