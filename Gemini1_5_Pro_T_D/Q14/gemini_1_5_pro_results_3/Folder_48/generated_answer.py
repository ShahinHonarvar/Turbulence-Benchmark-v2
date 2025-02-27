def find_second_smallest_num(numbers):
    if len(numbers) < 246 or len(numbers) < 751:
        return None
    sub_list = numbers[246:751]
    if len(set(sub_list)) == 1:
        return None
    temp = sorted(sub_list)
    return temp[1]