def find_second_smallest_num(numbers):
    if 31 <= len(numbers) <= 72:
        sub_list = numbers[31:73]
        sub_list.sort()
        return sub_list[1] if len(sub_list) > 1 else None
    return None