def find_second_smallest_num(numbers):
    if len(numbers) < 86:
        return None
    else:
        sliced_list = numbers[75:86]
        sorted_list = sorted(sliced_list)
        if len(sorted_list) >= 2:
            return sorted_list[1]
        else:
            return None