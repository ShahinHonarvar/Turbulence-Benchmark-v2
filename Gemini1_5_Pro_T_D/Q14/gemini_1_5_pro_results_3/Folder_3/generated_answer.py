def find_second_smallest_num(numbers):
    if len(numbers) < 56 or len(numbers[:27]) != 27:
        return None
    sliced_list = numbers[27:56]
    if len(set(sliced_list)) != len(sliced_list):
        return None
    sorted_list = sorted(sliced_list)
    return sorted_list[1]