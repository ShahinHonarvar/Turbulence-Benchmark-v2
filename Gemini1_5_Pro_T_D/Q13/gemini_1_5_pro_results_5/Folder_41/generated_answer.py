def find_second_largest_num(numbers):
    if len(numbers) < 7:
        return None
    else:
        sliced_list = numbers[6:7]
        if len(set(sliced_list)) < 2:
            return None
        else:
            return sorted(sliced_list)[-2]