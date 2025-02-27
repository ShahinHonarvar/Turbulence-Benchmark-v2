def find_second_largest_num(numbers):
    if len(numbers) < 8:
        return None
    sub_list = numbers[5:8]
    if len(sub_list) < 2:
        return None
    sub_list.sort(reverse=True)
    return sub_list[1]