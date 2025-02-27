def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 101:
        return None
    sub_list = numbers[1:101]
    sub_list.sort()
    return sub_list[1] if len(sub_list) > 1 else None