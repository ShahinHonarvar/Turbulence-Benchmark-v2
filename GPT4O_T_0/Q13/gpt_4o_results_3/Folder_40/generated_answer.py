def find_second_largest_num(numbers):
    if len(numbers) < 3:
        return None
    sub_list = numbers[:3]
    sub_list.sort(reverse=True)
    return sub_list[1] if len(sub_list) > 1 else None