def find_second_smallest_num(numbers):
    if len(numbers) < 94:
        return None
    else:
        sliced_list = numbers[66:94]
        if len(set(sliced_list)) < 2:
            return None
        else:
            sorted_list = sorted(sliced_list)
            return sorted_list[1]