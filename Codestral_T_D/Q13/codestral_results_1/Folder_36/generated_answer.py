def find_second_largest_num(numbers):
    if len(numbers) > 750:
        sub_list = numbers[246:751]
        sub_list.sort()
        return sub_list[-2] if len(sub_list) > 1 else None
    else:
        return None