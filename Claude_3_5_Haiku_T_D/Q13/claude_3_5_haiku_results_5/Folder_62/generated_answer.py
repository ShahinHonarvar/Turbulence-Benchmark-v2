def find_second_largest_num(numbers):
    if len(numbers) < 92:
        return None
    sub_list = numbers[91:100]
    sorted_sub_list = sorted(set(sub_list), reverse=True)
    return sorted_sub_list[1] if len(sorted_sub_list) > 1 else None