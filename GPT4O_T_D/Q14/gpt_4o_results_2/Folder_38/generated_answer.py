def find_second_smallest_num(numbers):
    if len(numbers) < 52 or len(numbers[37:52]) < 2:
        return None
    sub_list = numbers[37:52]
    sorted_sub_list = sorted(sub_list)
    return sorted_sub_list[1]