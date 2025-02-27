def find_second_smallest_num(numbers):
    if len(numbers) < 37:
        return None
    else:
        sliced_list = numbers[33:37]
        sorted_list = sorted(sliced_list)
        if len(sorted_list) < 2:
            return None
        else:
            return sorted_list[1]