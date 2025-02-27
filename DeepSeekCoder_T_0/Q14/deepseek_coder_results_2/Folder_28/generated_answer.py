def find_second_smallest_num(numbers):
    if len(numbers) < 51 or len(numbers) < 23:
        return None
    sub_list = numbers[22:51]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]