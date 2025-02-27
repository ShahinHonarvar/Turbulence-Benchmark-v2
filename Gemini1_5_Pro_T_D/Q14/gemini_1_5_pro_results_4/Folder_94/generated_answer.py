def find_second_smallest_num(numbers):
    if len(numbers) < 72:
        return None
    else:
        sliced_list = numbers[52:72]
        sliced_list.sort()
        if len(sliced_list) < 2:
            return None
        else:
            return sliced_list[1]