def find_second_smallest_num(numbers):
    if len(numbers) < 31 or len(numbers) < 21:
        return None
    sub_list = numbers[20:31]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]