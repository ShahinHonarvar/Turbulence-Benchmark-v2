def find_second_largest_num(numbers):
    if len(numbers) < 52:
        return None
    else:
        sliced_list = numbers[37:52]
        if len(set(sliced_list)) < 2:
            return None
        else:
            sliced_list.sort()
            return sliced_list[-2]