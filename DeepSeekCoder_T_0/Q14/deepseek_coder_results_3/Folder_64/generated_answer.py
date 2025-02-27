def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    sub_list = sorted(numbers[:5])
    return sub_list[1] if len(sub_list) > 1 else None