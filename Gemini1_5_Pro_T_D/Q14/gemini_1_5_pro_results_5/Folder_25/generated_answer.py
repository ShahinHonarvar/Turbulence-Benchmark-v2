def find_second_smallest_num(numbers):
    if len(numbers) < 77:
        return None
    else:
        sliced_list = numbers[37:77]
        sorted_list = sorted(sliced_list)
        if len(sorted_list) > 1:
            return sorted_list[1]
        else:
            return None