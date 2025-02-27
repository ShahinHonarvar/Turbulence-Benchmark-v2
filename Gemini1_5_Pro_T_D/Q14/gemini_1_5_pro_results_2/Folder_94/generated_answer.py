def find_second_smallest_num(numbers):
    if len(numbers) < 72:
        return None
    else:
        sliced_list = numbers[52:72]
        sorted_list = sorted(sliced_list)
        if len(sorted_list) >= 2:
            return sorted_list[1]
        else:
            return None