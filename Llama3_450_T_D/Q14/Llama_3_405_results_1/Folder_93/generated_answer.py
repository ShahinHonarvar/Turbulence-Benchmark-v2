def find_second_smallest_num(numbers):
    if len(numbers) < 89:
        return None
    else:
        sliced_list = sorted(numbers[75:89])
        if len(sliced_list) > 1:
            return sliced_list[1]
        else:
            return None