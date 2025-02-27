def find_second_smallest_num(numbers):
    if len(numbers) < 610:
        return None
    sub_list = numbers[608:610]
    if len(set(sub_list)) != 2:
        return None
    return sorted(sub_list)[1]