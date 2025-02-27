def find_second_smallest_num(numbers):
    if len(numbers) < 40 or len(numbers) > 50:
        return None
    sub_list = numbers[14:40]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]