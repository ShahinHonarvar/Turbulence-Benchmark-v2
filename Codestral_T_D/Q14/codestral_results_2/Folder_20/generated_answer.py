def find_second_smallest_num(numbers):
    if 75 <= len(numbers) <= 94:
        sub_list = sorted(numbers[75:95])
        return sub_list[1] if len(sub_list) > 1 else None
    else:
        return None