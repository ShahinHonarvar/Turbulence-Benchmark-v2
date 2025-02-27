def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 9:
        return None
    sub_list = sorted(numbers[:9])
    return sub_list[1] if len(sub_list) > 1 else None