def find_second_largest_num(numbers):
    if len(numbers) < 93 or len(numbers) < 13:
        return None
    sub_list = numbers[12:93]
    if len(set(sub_list)) < 2:
        return None
    largest_num = max(sub_list)
    sub_list.remove(largest_num)
    return max(sub_list)