def find_second_smallest_num(numbers):
    if 34 <= len(numbers) <= 55:
        sub_list = sorted(numbers[34:56])
        if len(sub_list) > 1:
            return sub_list[1]
    return None