def find_second_smallest_num(numbers):
    if 55 <= len(numbers) <= 98:
        sub_list = sorted(numbers[55:99])
        return sub_list[1] if len(sub_list) > 1 else None
    return None