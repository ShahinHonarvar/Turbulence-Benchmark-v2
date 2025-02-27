def find_second_smallest_num(numbers):
    if len(numbers) < 56:
        return None
    else:
        sliced_list = sorted(numbers[27:56])
        if len(sliced_list) < 2:
            return None
        else:
            return sliced_list[1]