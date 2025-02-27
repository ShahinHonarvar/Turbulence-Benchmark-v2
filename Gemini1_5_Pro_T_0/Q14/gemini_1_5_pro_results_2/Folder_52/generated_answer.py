def find_second_smallest_num(numbers):
    if len(numbers) < 67:
        return None
    else:
        sub_list = numbers[64:67]
        sub_list.sort()
        return sub_list[1] if len(sub_list) > 1 else None