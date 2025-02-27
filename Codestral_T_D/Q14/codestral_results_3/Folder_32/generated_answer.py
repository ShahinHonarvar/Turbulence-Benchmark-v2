def find_second_smallest_num(numbers):
    if len(numbers) <= 35:
        return None
    sub_list = sorted(numbers[32:36])
    return sub_list[1] if len(sub_list) > 1 else None