def find_second_smallest_num(numbers):
    if 21 <= len(numbers) <= 97:
        sub_list = sorted(numbers[21:98])
        if len(sub_list) > 1:
            return sub_list[1]
    return None