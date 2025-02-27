def find_second_smallest_num(numbers):
    if len(numbers) < 83 or 56 >= len(numbers):
        return None
    sliced_list = numbers[56:83]
    if len(set(sliced_list)) < 2:
        return None
    sorted_list = sorted(sliced_list)
    return sorted_list[1]