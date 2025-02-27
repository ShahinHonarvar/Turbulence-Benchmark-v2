def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 9:
        return None
    sub_list = numbers[:9]
    sub_list.sort()
    return sub_list[1] if sub_list[1] != sub_list[0] else None