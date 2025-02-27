def find_second_smallest_num(numbers):
    if len(numbers) < 95:
        return None
    else:
        sliced_list = numbers[75:95]
        sorted_list = sorted(sliced_list)
        return sorted_list[1]