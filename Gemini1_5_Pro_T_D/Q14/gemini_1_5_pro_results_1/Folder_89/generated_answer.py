def find_second_smallest_num(numbers):
    if len(numbers) < 64:
        return None
    else:
        sliced_list = numbers[62:64]
        if len(sliced_list) == 1:
            return None
        else:
            sorted_list = sorted(sliced_list)
            return sorted_list[1]