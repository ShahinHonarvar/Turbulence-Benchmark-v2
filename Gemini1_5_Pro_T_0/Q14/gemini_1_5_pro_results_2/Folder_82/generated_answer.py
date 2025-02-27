def find_second_smallest_num(numbers):
    if len(numbers) < 201:
        return None
    sliced_list = numbers[20:201]
    if len(set(sliced_list)) < 2:
        return None
    sorted_list = sorted(sliced_list)
    return sorted_list[1]