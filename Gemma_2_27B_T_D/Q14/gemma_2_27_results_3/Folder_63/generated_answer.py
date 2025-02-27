def find_second_smallest_num(numbers):
    if 56 < len(numbers) < 82:
        sub_list = numbers[56:83]
        if len(sub_list) > 1:
            return sorted(sub_list)[1]
    return None