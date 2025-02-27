def find_second_largest_num(numbers):
    if len(numbers) < 2 or 200 >= len(numbers):
        return None
    sub_list = numbers[200:201]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[-2]