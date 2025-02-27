def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    sliced_list = numbers[686:988]
    if len(sliced_list) < 2:
        return None
    sorted_list = sorted(sliced_list)
    return sorted_list[1]