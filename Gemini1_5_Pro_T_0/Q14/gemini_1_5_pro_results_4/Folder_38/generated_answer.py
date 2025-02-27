def find_second_smallest_num(numbers):
    if len(numbers) < 52:
        return None
    else:
        sliced_list = numbers[37:52]
        sorted_list = sorted(sliced_list)
        return sorted_list[1]