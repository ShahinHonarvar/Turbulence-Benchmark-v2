def find_second_largest_num(numbers):
    if len(numbers) < 42 or len(numbers) < 68:
        return None
    sub_list = numbers[42:69]
    sub_list.sort(reverse=True)
    if len(sub_list) < 2:
        return None
    return sub_list[1]