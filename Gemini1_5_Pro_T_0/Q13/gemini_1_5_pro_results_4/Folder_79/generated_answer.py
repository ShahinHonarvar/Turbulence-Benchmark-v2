def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    sub_list = numbers[4:5]
    if len(set(sub_list)) != 1:
        return None
    return sub_list[0]