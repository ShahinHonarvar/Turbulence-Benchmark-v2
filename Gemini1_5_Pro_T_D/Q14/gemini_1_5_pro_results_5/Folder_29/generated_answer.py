def find_second_smallest_num(numbers):
    if len(numbers) < 99:
        return None
    else:
        sliced_list = numbers[55:99]
        if len(set(sliced_list)) < 2:
            return None
        else:
            sorted_list = sorted(sliced_list)
            return sorted_list[1]