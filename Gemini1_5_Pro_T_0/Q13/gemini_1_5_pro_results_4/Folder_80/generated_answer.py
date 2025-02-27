def find_second_largest_num(numbers):
    if len(numbers) < 67:
        return None
    sub_list = numbers[64:67]
    if len(set(sub_list)) < 2:
        return None
    sub_list.sort()
    return sub_list[1]