def find_second_largest_num(numbers):
    if len(numbers) < 86:
        return None
    sub_list = numbers[75:86]
    unique_sub_list = sorted(set(sub_list), reverse=True)
    return unique_sub_list[1] if len(unique_sub_list) > 1 else None