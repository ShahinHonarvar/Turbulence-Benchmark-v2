def find_second_smallest_num(numbers):
    if len(numbers) < 41:
        return None
    else:
        sliced_list = numbers[28:41]
        sorted_list = sorted(sliced_list)
        if len(sorted_list) < 2:
            return None
        else:
            return sorted_list[1]