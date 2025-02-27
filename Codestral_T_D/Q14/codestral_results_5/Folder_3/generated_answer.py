def find_second_smallest_num(numbers):
    if 27 <= len(numbers) <= 55:
        sub_list = sorted(numbers[27:56])
        if len(sub_list) > 1:
            return sub_list[1]
    return None